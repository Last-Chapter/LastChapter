# Generated by Django 4.0.7 on 2023-03-08 12:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=127)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('genre', models.CharField(choices=[('Aventura', 'Adventure'), ('Arte ou Cinema', 'Art Cinema'), ('Biografia', 'Biography'), ('Negócios', 'Business'), ('Infantil', 'Childish'), ('Quadrinhos', 'Comic Book'), ('Computação', 'Computing'), ('Policial', 'Detective'), ('Educativo', 'Educational'), ('Ficção', 'Fiction'), ('Literatura Estrangeira', 'Foreign Literature'), ('Geek', 'Geek'), ('Saúde', 'Health'), ('História', 'History'), ('LGBTQIA+', 'Lgbtqia Plus'), ('Literatura Nacional', 'National Literature'), ('Política', 'Policy'), ('Religioso', 'Religious'), ('Romance', 'Romance'), ('Ciências', 'Science'), ('Jovens e Adolescentes', 'Young Adult'), ('Outros', 'Default')], default='Outros', max_length=50)),
                ('launch_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_followed', to='books.book')),
            ],
        ),
    ]
