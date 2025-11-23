# api/views.py
from rest_framework import generics, viewsets # <--- Import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

# Existing View from Task 1
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for Task 2
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]