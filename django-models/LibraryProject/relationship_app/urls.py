# in relationship_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Path for the function-based book list view
    # e.g., http://127.0.0.1:8000/books/
    path('books/', views.book_list_view, name='book-list'),
    
    # Path for the class-based library detail view
    # <int:pk> captures the library's ID from the URL
    # e.g., http://127.0.0.1:8000/library/1/
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]