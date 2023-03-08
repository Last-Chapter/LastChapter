from django.db import models
import uuid


class Address(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    street = models.CharField(max_length=127)
    number = models.IntegerField()
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    code_zip = models.CharField(max_length=10)

    def __repr__(self) -> str:
        return f"<Address ({self.id}) - {self.street}, {self.number}>"
