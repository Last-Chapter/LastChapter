from .models import Copy
from django.shortcuts import render
from rest_framework import generics
from .serializers import CopySerializer
from .permissions import IsAccountOwnerOrAdmin
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication


class CopyView(generics.ListCreateAPIView):

    def get_queryset(self):
        return self.queryset.filter(book=self.kwargs.get("book_id"))

    def perform_create(self, serializer):
        return serializer.save(book=self.kwargs.get("book_id"))

    copies = Copy.objects.all()
    serializer_class = CopySerializer

    permission_classes = [IsAccountOwnerOrAdmin]
    authentication_classes = [JWTAuthentication]


class CopyDetailView(generics.ListCreateAPIView):

    copies = Copy.objects.all()
    serializer_class = CopySerializer

    permission_classes = [IsAccountOwnerOrAdmin]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(book=self.kwargs.get("pk"))
