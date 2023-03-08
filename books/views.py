from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from permissions.isAccountOwnerOrAdmin import IsAccountOwnerOrAdmin


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdmin]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    lookup_url_kwarg = "book_id"
