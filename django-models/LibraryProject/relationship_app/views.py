# in relationship_app/views.py

from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# 1. Function-Based View (FBV) for listing all books
def book_list_view(request):
    # Get all books from the database
    books = Book.objects.all()
    
    # Create the context (data to pass to the template)
    context = {
        'books': books
    }
    
    # Render the template with the context
    return render(request, 'relationship_app/list_books.html', context)


# 2. Class-Based View (CBV) for a single library's details
class LibraryDetailView(DetailView):
    # Tell the view which model it's working with
    model = Library
    
    # Tell the view which template to use
    template_name = 'relationship_app/library_detail.html'
    
    # Tell the view what to call the object in the template
    # (The template uses 'library', so we set this)
    context_object_name = 'library'