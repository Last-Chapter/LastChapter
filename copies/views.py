from .models import Copy
from books.models import Book
from django.shortcuts import render
from rest_framework import generics
from .serializers import CopySerializer
from .permissions import IsAccountOwnerOrAdmin
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication


class CopyView(generics.CreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer
    lookup_url_kwarg = "book_id"

    permission_classes = [IsAccountOwnerOrAdmin]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        book_id = self.kwargs["book_id"]
        book = Book.objects.get(id=book_id)

        serializer.save(book=book)


class CopyListView(generics.ListAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    permission_classes = [IsAccountOwnerOrAdmin]
    authentication_classes = [JWTAuthentication]


class CopyDetailView(generics.ListCreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    permission_classes = [IsAccountOwnerOrAdmin]
    authentication_classes = [JWTAuthentication]
