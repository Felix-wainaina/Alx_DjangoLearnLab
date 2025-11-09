# In relationship_app/views.py

# --- IMPORTS (ALL IN ONE PLACE) ---
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