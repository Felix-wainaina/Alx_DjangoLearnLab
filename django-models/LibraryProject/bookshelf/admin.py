# bookshelf/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = ("title", "author", "publication_year")

    # Add a search box for quick lookups by title or author
    search_fields = ("title", "author")

    # Filter sidebar to narrow down by publication year
    list_filter = ("publication_year",)

    # Optional UX improvements
    ordering = ("-publication_year", "title")
    list_per_page = 25
