from copies.models import Copy
from rest_framework import serializers
from users.serializers import UserSerializer
from rest_framework.views import APIView, Request, Response, status


class CopySerializer(serializers.Serializer):

    class Meta:
        model = Copy
        fields = ["id", "created_at", "is_available",]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data: dict) -> Copy:
        return Copy.objects.create(**validated_data)
