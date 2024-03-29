from django.db import models
import uuid


class Genres(models.TextChoices):
    ADVENTURE = ("Aventura",)
    ART_CINEMA = ("Arte ou Cinema",)
    BIOGRAPHY = ("Biografia",)
    BUSINESS = ("Negócios",)
    CHILDISH = ("Infantil",)
    COMIC_BOOK = ("Quadrinhos",)
    COMPUTING = ("Computação",)
    DETECTIVE = ("Policial",)
    EDUCATIONAL = ("Educativo",)
    FICTION = ("Ficção",)
    FOREIGN_LITERATURE = ("Literatura Estrangeira",)
    GEEK = ("Geek",)
    HEALTH = ("Saúde",)
    HISTORY = ("História",)
    LGBTQIA_plus = ("LGBTQIA+",)
    NATIONAL_LITERATURE = ("Literatura Nacional",)
    POLICY = ("Política",)
    RELIGIOUS = ("Religioso",)
    ROMANCE = ("Romance",)
    SCIENCE = ("Ciências",)
    YOUNG_ADULT = ("Jovens e Adolescentes",)
    DEFAULT = "Outros"


class Book(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=50)
    description = models.TextField(null=True)
    genre = models.CharField(
        max_length=50,
        choices=Genres.choices,
        default=Genres.DEFAULT,
    )
    launch_year = models.IntegerField()

    user_followers = models.ManyToManyField(
        "users.User",
        through="Following",
        related_name="book_followers",
    )

    def __repr__(self) -> str:
        return f"<{self.id} - {self.title}>"


class Following(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="book_followed",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="followed_by",
    )
