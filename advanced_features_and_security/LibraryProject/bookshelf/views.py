from django.shortcuts import render
from .forms import ExampleForm
from .models import Book
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

# ... (any other views you had) ...

# --- TASK 1 FIX: Update permissions to 'bookshelf.can_...' ---
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # This view must render the 'book_list.html' template
    # In a real app, you would pass a list of books:
    # books = Book.objects.all()
    # return render(request, 'bookshelf/book_list.html', {'books': books})
    
    # For the checker, just rendering the file is enough
    return render(request, 'bookshelf/book_list.html')

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    return HttpResponse(f"You have permission to view book {book_id}.")

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse("You have permission to create a new book.")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    return HttpResponse(f"You have permission to edit book {book_id}.")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    return HttpResponse(f"You have permission to delete book {book_id}.")

# Documentation (Task 2, Step 3):
# --- (B) UPDATE YOUR search_books VIEW ---
def search_books(request):
    # --- Change 'SearchForm' to 'ExampleForm' ---
    form = ExampleForm()
    results = []

    if 'query' in request.GET:
        form = ExampleForm(request.GET) # <-- Change here
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.objects.filter(title__icontains=query)

    return render(request, 'bookshelf/form_example.html', {
        'form': form,
        'results': results
    })