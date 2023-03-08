from rest_framework import serializers
from .models import Book
from users.serializers import UserSerializer


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "description",
            "genre",
            "launch_year",
            "user_followers",
        ]
        read_only_fields = ["id", "user_followers"]
