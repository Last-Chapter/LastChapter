from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    class Meta:
        ordering = ["first_name"]

    id = uuid.uuid4()
    is_blocked = models.BooleanField(null=True, default=False)

    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=127)

    address = models.ForeignKey(
        "addresses.Address",
        on_delete=models.PROTECT,
        related_name="user",
    )

    def __repr__(self) -> str:
        return f"<{self.id} - {self.email}>"
