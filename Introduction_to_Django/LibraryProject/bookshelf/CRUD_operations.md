# CRUD_operations.md

Create
Command:

Python

# First, import the model
from bookshelf.models import Book

# Create a new book instance in memory
book = Book(title="1984", author="George Orwell", publication_year=1949)

# Save the instance to the database
book.save()
Output:

# After running book.save(), there is no direct output,
# but the command completes successfully.
# You will just be returned to the '>>>' prompt.
Retrieve
Command:

Python

# Make sure you've imported the model (if in a new shell session)
from bookshelf.models import Book

# Retrieve the specific book
b = Book.objects.get(title="1984")

# Print its attributes
print(f"Title: {b.title}, Author: {b.author}, Year: {b.publication_year}")
Output:

Title: 1984, Author: George Orwell, Year: 1949
Update
Command:

Python

# Make sure you've imported the model
from bookshelf.models import Book

# First, retrieve the book you want to update
book_to_update = Book.objects.get(title="1984")

# Change the title attribute in Python
book_to_update.title = "Nineteen Eighty-Four"

# Save the changes back to the database
book_to_update.save()

# (Optional) Verify the change
updated_book = Book.objects.get(id=book_to_update.id)
print(updated_book.title)
Output:

Nineteen Eighty-Four
Delete
Command:

Python

# Make sure you've imported the model
from bookshelf.models import Book

# First, retrieve the book you want to delete
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")

# Call the delete() method
book_to_delete.delete()

# (Optional) Confirm by trying to retrieve all books
all_books = Book.objects.all()
print(all_books)
Output:

# The output of the .delete() command is a tuple
# showing what was deleted.
(1, {'bookshelf.Book': 1})

# The output of the print(all_books) command will be:
<QuerySet []>