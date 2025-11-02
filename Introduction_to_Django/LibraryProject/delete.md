# delete.md

**Command executed in Django shell:**
```python
from bookshelf.models import Book
b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
Book.objects.all()

# b.delete() returns something like:
(1, {'bookshelf.Book': 1})
# indicating one Book was deleted.

# QuerySet after deletion:
<QuerySet []>
