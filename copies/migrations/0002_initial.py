# Generated by Django 4.1.7 on 2023-03-10 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("copies", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="copy",
            name="user_borrowers",
            field=models.ManyToManyField(
                related_name="copy_borrowers",
                through="copies.Borrowing",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="borrowing",
            name="copy",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="borrowed_copy",
                to="copies.copy",
            ),
        ),
        migrations.AddField(
            model_name="borrowing",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="borrowed_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
