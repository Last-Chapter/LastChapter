from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
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
            "email",
            "password",
            "is_superuser",
            "is_staff",
            "first_name",
            "last_name",
            "is_active",
            "is_blocked",
            "address_id",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True},
            "is_staff": {"read_only": True},
        }

    def create(self, validated_data: dict) -> User:
        create_user = User.objects.create(**validated_data)
        create_user.is_staff = create_user.is_superuser
        create_user.password = make_password(create_user.password)
        create_user.save()

        return create_user

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(str(password))

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
