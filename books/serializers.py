from rest_framework import serializers
from .models import Book, Following


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


class BookFollowingSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="book.title", read_only=True)
    followed_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data: dict) -> Following:
        return Following.objects.create(**validated_data)

    class Meta:
        model = Following
        fields = ["id", "book", "user", "title", "followed_by"]
        read_only_fields = ["id", "book", "user", "title", "followed_by"]
