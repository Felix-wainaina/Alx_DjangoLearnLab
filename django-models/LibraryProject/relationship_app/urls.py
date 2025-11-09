# in relationship_app/urls.py

from django.urls import path
# --- THIS IS THE FIX ---
# Import each view by its specific name
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Path for the function-based book list view
    # Use 'list_books' directly (no 'views.')
    path('books/', list_books, name='book-list'), # <-- CHANGED
    
    # Path for the class-based library detail view
    # Use 'LibraryDetailView' directly
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'), # <-- CHANGED
]