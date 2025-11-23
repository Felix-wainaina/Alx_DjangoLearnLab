# api/urls.py
from django.urls import path, include # <--- Import include
from rest_framework.routers import DefaultRouter # <--- Import DefaultRouter
from .views import BookList, BookViewSet

# Create the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing Path from Task 1
    path('books/', BookList.as_view(), name='book-list'),

    # New Router Paths for Task 2
    path('', include(router.urls)), 
]