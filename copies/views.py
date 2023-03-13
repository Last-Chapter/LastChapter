from .models import Copy, Borrowing
from books.models import Book
from users.models import User
from rest_framework import generics
from .serializers import CopySerializer, CopyBorrowingSerializer
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404
from datetime import date, timedelta
from rest_framework.exceptions import NotAcceptable
from permissions.isBlockedOrNot import IsBlockedOrNot


class CopyView(generics.ListCreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer
    lookup_url_kwarg = "book_id"

    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        book_id = self.kwargs["book_id"]
        book = Book.objects.get(id=book_id)

        serializer.save(book=book)


class CopyListView(generics.ListAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]


class CopyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = CopySerializer

    lookup_url_kwarg = "copy_id"

    def perform_create(self, serializer):
        copy_id = self.kwargs["copy_id"]
        copy = Copy.objects.get(id=copy_id)
        serializer.save(copy=copy)

    def perform_destroy(self, instance: Copy):
        instance.delete()


class CopyBorrowingView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request, copy_id):
        copy = get_object_or_404(Copy, id=copy_id)
        user:User = request.user

        today = date.today() + timedelta(days=15)
        
        if user.blocked_until and today > user.blocked_until.date():
            user.blocked_until = None
            user.is_blocked = False
            user.save()

        if user.is_blocked :

            raise NotAcceptable("Account has been blocked")

        if not copy.is_available:
            raise NotAcceptable("The copy is not available")

        serializer = CopyBorrowingSerializer(data=dict())

        serializer.is_valid(raise_exception=True)

        copy.is_available = False
        copy.save()

        serializer.save(copy=copy, user=user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def patch(self, request, copy_id):
        borrowing = get_object_or_404(Borrowing, copy=copy_id)

        today = date.today()
        """precisa coloca a logica de envia o email 
           para o cliente quando tiver a copia disponivel
        """
        borrowing.returned_at = today

        user = get_object_or_404(User, pk=request.user.id)

        is_late = today > borrowing.should_return_at

        if is_late:
            blocked_until = today + timedelta(days=10)
            user.blocked_until = blocked_until
            user.is_blocked = True
            user.save()

        copy = Copy.objects.get(id=copy_id)

        copy.is_available = True

        copy.save()

        borrowing.save()

        serializer = CopyBorrowingSerializer(borrowing)

        return Response(serializer.data)
