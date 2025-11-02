# create.md

**Command executed in Django shell:**
```python
from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
b

# The create() returns the created Book instance.
# Printing the instance will display:
1984
# or in some shells:
# <Book: 1984>