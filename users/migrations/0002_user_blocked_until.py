# Generated by Django 4.1.7 on 2023-03-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="blocked_until",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
