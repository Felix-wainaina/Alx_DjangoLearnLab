# In relationship_app/views.py

# --- IMPORTS (ALL IN ONE PLACE) ---
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm

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