# retrieve.md

**Command executed in Django shell:**
```python
from bookshelf.models import Book
qs = Book.objects.all()
qs
b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year

# QuerySet shows the stored book:
<QuerySet [<Book: 1984>]>

# Accessing attributes:
('1984', 'George Orwell', 1949)