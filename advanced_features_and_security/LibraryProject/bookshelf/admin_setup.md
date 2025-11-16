# admin_setup.md

## Purpose
Register the `Book` model in Django admin and configure the change list for better management and visibility.

## File changed
- `bookshelf/admin.py`

## Admin configuration
```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)
    ordering = ("-publication_year", "title")
    list_per_page = 25
