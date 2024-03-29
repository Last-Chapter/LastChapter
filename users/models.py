from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    blocked_until = models.DateTimeField(null=True, blank=True)
    is_blocked = models.BooleanField(null=True, default=False)
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=127)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    username = None

    address = models.ForeignKey(
        "addresses.Address",
        on_delete=models.PROTECT,
        related_name="users",
        null=True,
    )

    def __repr__(self) -> str:
        return f"<{self.id} - {self.email}>"
