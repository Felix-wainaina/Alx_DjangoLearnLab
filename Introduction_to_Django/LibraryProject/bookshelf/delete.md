# delete.md

**Command executed in Django shell:**
```python
# Make sure you've imported the model
from bookshelf.models import Book

# First, retrieve the book you want to delete
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")

# Call the delete() method
book_to_delete.delete()

# (Optional) Confirm by trying to retrieve all books
all_books = Book.objects.all()
print(all_books)

# The output of the .delete() command is a tuple
# showing what was deleted.
(1, {'bookshelf.Book': 1})

# The output of the print(all_books) command will be:
<QuerySet []>