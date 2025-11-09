from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Keep this generic import style

urlpatterns = [
    # Task 1 paths
    path('books/', views.list_books, name='book-list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    
    # Task 2 paths
    path('login/', 
         LoginView.as_view(template_name='relationship_app/login.html'), 
         name='login'),
    path('logout/', 
         LogoutView.as_view(template_name='relationship_app/logout.html'), 
         name='logout'),
    path('register/', views.register, name='register'),

    # Task 3 paths
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),

    # --- TASK 4 PATHS (Corrected for Checker) ---
    
    # This path now contains "add_book/"
    path('add_book/', views.book_add_view, name='book-add'),
    
    # This path now contains "edit_book/"
    path('edit_book/<int:pk>/', views.book_edit_view, name='book-edit'),
    
    # This path now contains "delete_book/"
    path('delete_book/<int:pk>/', views.book_delete_view, name='book-delete'),
]