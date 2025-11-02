# update.md

**Command executed in Django shell:**
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

Book.objects.all()


#After saving the instance, the updated title is visible:

<QuerySet [<Book: Nineteen Eighty-Four>]>