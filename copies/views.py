from .models import Copy, Borrowing
from books.models import Book
from rest_framework import generics
from .serializers import CopySerializer, CopyBorrowingSerializer
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404
from datetime import date
from rest_framework.exceptions import NotAcceptable


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

        if not copy.is_available:
            raise NotAcceptable("A copia não esta disponivel")

        user = request.user

        serializer = CopyBorrowingSerializer(data=dict())

        serializer.is_valid(raise_exception=True)

        copy.is_available = False
        copy.save()

        serializer.save(copy=copy, user=user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def patch(self, req, copy_id):
        borrowing = get_object_or_404(Borrowing, copy=copy_id)
        today = date.today()
        borrowing.returned_at = today
        borrowing.save()
        serializer = CopyBorrowingSerializer(borrowing)
        return Response(serializer.data)
