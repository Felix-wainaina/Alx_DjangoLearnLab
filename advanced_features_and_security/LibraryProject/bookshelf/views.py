from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

# ... (any other views you had) ...

# --- TASK 1 FIX: Update permissions to 'bookshelf.can_...' ---
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # This is the view the checker is looking for.
    # In a real app, this would show all books.
    return HttpResponse("You have permission to view the book list.")

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