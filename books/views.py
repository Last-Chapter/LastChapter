from rest_framework import generics
from rest_framework.views import APIView, Response, Request, status
from .models import Book
from .serializers import BookSerializer, BookFollowingSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from permissions.isAccountOwnerOrAdmin import IsAccountOwnerOrAdmin
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotAcceptable


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        data_book = self.request.data
        title = data_book["title"]
        author = data_book["author"]
        book = Book.objects.filter(
            title=title,
            author=author,
        ).first()
        if book:
            raise NotAcceptable("This book is already registered")

        serializer.save()


class BookDetailView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdmin]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    lookup_url_kwarg = "book_id"


class BookFollowingView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request: Request, book_id):
        book = get_object_or_404(Book, id=book_id)

        user = request.user
        serializer = BookFollowingSerializer(data=dict())
        serializer.is_valid()
        serializer.save(book=book, user=user)

        return Response(serializer.data, status.HTTP_201_CREATED)
