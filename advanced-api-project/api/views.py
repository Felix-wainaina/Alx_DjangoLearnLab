# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Import the necessary backends
from django_filters import rest_framework
from rest_framework import filters

class BookListView(generics.ListAPIView):
    """
    View to list all books.
    Supports:
    - Filtering by title, author, and publication_year
    - Searching by title and author's name
    - Ordering by title and publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Add the filter backends
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # 1. Configure Filtering (Exact matches)
    # Allows requests like: /books/?title=Harry%20Potter
    filterset_fields = ['title', 'author', 'publication_year']

    # 2. Configure Searching (Text search)
    # Allows requests like: /books/?search=Potter
    # Note: 'author__name' allows searching by the related author's name field
    search_fields = ['title', 'author__name']

    # 3. Configure Ordering
    # Allows requests like: /books/?ordering=publication_year
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] # Default ordering