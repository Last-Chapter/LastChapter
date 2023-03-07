from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=127)
    number = models.IntegerField()
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    code_zip = models.CharField(max_length=10)

    def __repr__(self) -> str:
        return f"<Address ({self.id}) - {self.street}, {self.number}>"
