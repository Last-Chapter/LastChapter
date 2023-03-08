from django.db import models
import uuid


class Copy(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    created_at = models.DateField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copies",
    )

    user_borrowers = models.ManyToManyField(
        "users.User", through="Borrowing", related_name="copy_borrowers"
    )

    def __repr__(self) -> str:
        return f"<{self.id} - {self.is_available}>"


class Borrowing(models.Model):
    copy = models.ForeignKey(
        "copies.Copy",
        on_delete=models.CASCADE,
        related_name="borrowed_copy",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="borrowed_by",
    )

    borrowed_at = models.DateField(auto_now_add=True)
    should_returned_at = models.DateField(null=True, default=None)

