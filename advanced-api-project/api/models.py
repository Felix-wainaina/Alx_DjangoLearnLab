# api/models.py
from django.db import models

class Author(models.Model):
    """
    The Author model represents a writer.
    It has a one-to-many relationship with the Book model.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model represents a literary work.
    It is linked to an Author via a ForeignKey.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title