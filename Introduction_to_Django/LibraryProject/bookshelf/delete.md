# delete.md

**Command executed in Django shell:**
```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()

###Expected output (commented):

book.delete() returns something like:

(1, {'bookshelf.Book': 1})

QuerySet after deletion:

<QuerySet []>