# In relationship_app/urls.py

from django.urls import path
# We don't need the built-in views anymore for this
from django.contrib.auth.views import LoginView 

# Import ALL your views from views.py
from .views import list_books, LibraryDetailView, register, custom_logout_view

urlpatterns = [
    # Your previous paths
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    
    # LOGIN (keeps using the built-in view)
    path('login/', 
         LoginView.as_view(template_name='relationship_app/login.html'), 
         name='login'),
         
    # LOGOUT (now points to your new custom view)
    path('logout/', custom_logout_view, name='logout'),
         
    # REGISTER
    path('register/', register, name='register'),
]