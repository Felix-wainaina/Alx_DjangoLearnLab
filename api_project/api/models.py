# api/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # CharField for title
    author = models.CharField(max_length=100) # CharField for author

    def __str__(self):
        return self.title