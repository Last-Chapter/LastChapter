from copies.models import Copy
from rest_framework import serializers
from rest_framework.views import APIView, Request, Response, status
from copies.models import Borrowing
from datetime import date, timedelta


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
    returned_at = serializers.DateField(default=None)

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
        read_only_fields = [
            "id",
            "copy",
            "user",
            "borrowed_at",
            "should_return_at",
        ]

    def create(self, validated_data):
        should_return_at = validated_data.get('should_return_at')

        if should_return_at.weekday() > 4 :
            days_to_add = 7 - should_return_at.weekday()
            should_return_at += timedelta(days=days_to_add)
        validated_data['should_return_at'] = should_return_at

        borrowing = Borrowing.objects.create(**validated_data)
        return borrowing
