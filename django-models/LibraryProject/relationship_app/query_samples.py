# relationship_app/query_samples.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Prepare sample data
author, _ = Author.objects.get_or_create(name="Jane Doe")
book1, _ = Book.objects.get_or_create(title="Django Uncovered", author=author)
book2, _ = Book.objects.get_or_create(title="Advanced Django", author=author)

library, _ = Library.objects.get_or_create(name="Central Library")
library.books.add(book1)

if not hasattr(library, 'librarian'):
    Librarian.objects.create(name="Mary the Librarian", library=library)

# --- ALX Checker queries ---
library_name = "Central Library"
author_name = "Jane Doe"

# 1) List all books in a library
library = Library.objects.get(name=library_name)
for b in library.books.all():
    print(" -", b.title)

# 2) Query all books by a specific author
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
for b in books_by_author:
    print(" -", b.title)

# 3) Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian:", librarian.name)
