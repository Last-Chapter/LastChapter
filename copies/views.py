from .models import Copy
from books.models import Book
from django.shortcuts import render
from rest_framework import generics
from .serializers import CopySerializer
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
# from permissions.isStaffAndAdmin import IsStaffAndAdmin
from rest_framework.permissions import IsAdminUser, IsAuthenticated


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
