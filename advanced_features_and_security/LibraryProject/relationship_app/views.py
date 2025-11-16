# In relationship_app/views.py

# --- IMPORTS (ALL IN ONE PLACE) ---
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
# This is the decorator the task requires
from django.contrib.auth.decorators import permission_required

# --- FORM FOR ADDING/EDITING BOOKS ---
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

# --- YOUR EXISTING VIEWS (from Task 1) ---

# 1. Function-based View
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


# 2. Class-based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'


# --- NEW AUTHENTICATION VIEW (from Task 2) ---

# 3. Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in immediately
            return redirect("book-list") # Redirect to your book list page
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# --- ADD THIS NEW VIEW AT THE BOTTOM ---
def custom_logout_view(request):
    logout(request)
    # Now, render the 'logged out' page
    return render(request, "relationship_app/logout.html")


# --- TASK 3: ROLE-BASED ACCESS CONTROL VIEWS ---
# Step 2: Helper functions for @user_passes_test
# These functions check the user's role.
# We check 'is_authenticated' first to avoid errors with anonymous users.
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

# Step 2: Set Up Role-Based Views
# The decorator @user_passes_test checks the role before running the view.
# 'login_url' redirects them to the login page if they fail the test.

@login_required
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# --- TASK 4: VIEWS WITH CUSTOM PERMISSIONS ---

@login_required
@permission_required('relationship_app.can_add_book', login_url='/login/')
def book_add_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

@login_required
@permission_required('relationship_app.can_change_book', login_url='/login/')
def book_edit_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm(instance=book)
    # 'object' is used in the template to check if we are editing
    return render(request, 'relationship_app/book_form.html', {'form': form, 'object': book})

@login_required
@permission_required('relationship_app.can_delete_book', login_url='/login/')
def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    # 'object' is used in the template to show the book's name
    return render(request, 'relationship_app/book_confirm_delete.html', {'object': book})

# --- ADD THIS NEW CODE AT THE END OF THE FILE ---

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

# Documentation for views (Task 1, Step 5)
# These views enforce permissions using the @permission_required decorator.
# The 'raise_exception=True' argument will show a 403 Forbidden page
# if the user does not have the required permission.

@permission_required('relationship_app.can_view', raise_exception=True)
def view_book(request, book_id):
    # In a real app, you'd fetch the book:
    # book = Book.objects.get(pk=book_id)
    return HttpResponse(f"You have permission to view book {book_id}.")

@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    # In a real app, you'd show a form:
    # form = BookForm()
    return HttpResponse("You have permission to create a new book.")

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # In a real app, you'd show a form for a specific book:
    # book = Book.objects.get(pk=book_id)
    # form = BookForm(instance=book)
    return HttpResponse(f"You have permission to edit book {book_id}.")

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # In a real app, you'd show a confirmation page:
    # book = Book.objects.get(pk=book_id)
    return HttpResponse(f"You have permission to delete book {book_id}.")
