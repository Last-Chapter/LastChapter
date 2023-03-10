from copies.models import Copy
from rest_framework import serializers
from rest_framework.views import APIView, Request, Response, status
from copies.models import Borrowing
from datetime import date, timedelta
from rest_framework.exceptions import NotAcceptable


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ["id", "created_at", "is_available", "book_id"]
        read_only_fields = ["id", "created_at", "book_id"]


class CopyBorrowingSerializer(serializers.ModelSerializer):
    copy = (serializers.CharField(source="copy.id", read_only=True),)
    user = (serializers.CharField(source="user.email", read_only=True),)

    borrowed_at = (serializers.DateField(default=date.today),)
    should_return_at = serializers.DateField(
        default=lambda: date.today() + timedelta(days=15)
    )
    returned_at = serializers.DateField()

    class Meta:
        model = Borrowing
        fields = [
            "id",
            "copy",
            "user",
            "borrowed_at",
            "returned_at",
            "should_return_at",
        ]
        read_only_fields = ["id", "copy", "user", "borrowed_at", "should_return_at"]

    def create(self, validated_data):
        borrowing = Borrowing.objects.create(**validated_data)
        return borrowing

    def update(self, instance: Borrowing, validated_data: dict):
        for key, value in validated_data.items():
            if key.returned_at:
                setattr(instance, key, value)
            else:
                raise NotAcceptable("Not acceptable")

        instance.save()

        return instance
