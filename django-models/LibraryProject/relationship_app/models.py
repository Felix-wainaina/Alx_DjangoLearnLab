# relationship_app/models.py
from django.db import models
from django.contrib.auth import get_user_model

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    publication_year = models.IntegerField(default=2000)  # <-- ADD THIS LINE

    def __str__(self):
        return f"{self.title} (by {self.author.name})"

class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(
        Book,
        related_name='libraries',
        blank=True
    )

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name='librarian'
    )

    def __str__(self):
        return f"{self.name} — {self.library.name}"
