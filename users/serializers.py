from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

# from addresses.serializers import AddressSerializer


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="This username has already taken"
            )
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="This e-mail has already taken"
            )
        ]
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_superuser",
            "first_name",
            "last_name",
            "is_active",
            "is_blocked",
            "address_id",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True},
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(str(password))

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
