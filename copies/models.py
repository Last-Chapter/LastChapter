from django.db import models

class Copy(models.Model):
    class Meta:
        ordering = ["id"]

    created_at = models.DateField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    book = models.ForeignKey(
        "books.Book",
        on_delete = models.CASCADE,
        related_name = "copies", 
    )


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
    returned_at = models.DateField(null=True, default=None)
