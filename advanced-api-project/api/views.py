# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    View to list all books.
    Access: Public (AllowAny) by default, or ReadOnly.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Explicitly allowing read-only access to unauthenticated users
    permission_classes = [IsAuthenticatedOrReadOnly] 

class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book by ID.
    Access: Public (AllowAny) by default, or ReadOnly.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book.
    Access: Authenticated users only.
    Customization: Standard validation logic is handled by the serializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Locks this view

    def perform_create(self, serializer):
        # This hook allows custom logic during creation
        # Example: We could assign the current user as the adder of the book if we had that field
        serializer.save() 

class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book.
    Access: Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Custom logic for updating could go here
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book.
    Access: Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]