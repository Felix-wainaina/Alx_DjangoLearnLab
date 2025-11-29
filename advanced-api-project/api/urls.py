# api/urls.py
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # List all books: GET /books/
    path('books/', BookListView.as_view(), name='book-list'),

    # Retrieve a single book: GET /books/{id}/
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a new book: POST /books/create/
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update a book: PUT/PATCH /books/update/{id}/
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # Delete a book: DELETE /books/delete/{id}/
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]