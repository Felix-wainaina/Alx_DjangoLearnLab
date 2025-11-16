from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

# Register your new model
admin.site.register(UserProfile)
