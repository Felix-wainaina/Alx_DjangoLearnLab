from django.urls import path
from . import views

urlpatterns = [
    path('book/create/', views.create_book, name='create_book'),
    path('book/<int:book_id>/view/', views.view_book, name='view_book'),
    path('book/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]