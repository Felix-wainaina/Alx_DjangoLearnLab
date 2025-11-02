# update.md

**Command executed in Django shell:**
```python
from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.all()

# After saving the instance, the updated title is visible:
<QuerySet [<Book: Nineteen Eighty-Four>]>
