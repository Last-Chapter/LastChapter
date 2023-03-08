from rest_framework import serializers
from .models import Address
from users.models import User
from users.serializers import UserSerializer


class AddressSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    # users = UserSerializer(
    #     many=True,
    #     read_only=True,
    # )

    class Meta:
        model = Address
        fields = [
            "id",
            "street",
            "number",
            "district",
            "city",
            "users",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
        }

    def create(self, validated_data: dict) -> Address:
        user = User.objects.get(id=self.context["request"].user.id)
        create_address = Address.objects.create(**validated_data)
        user.address = create_address
        user.save()
        return create_address

    def get_users(self, obj):
        return [user.id for user in obj.users.all()]
