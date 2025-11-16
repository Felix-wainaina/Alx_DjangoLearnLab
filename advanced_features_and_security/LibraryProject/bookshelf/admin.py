# bookshelf/admin.py
from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = ("title", "author", "publication_year")

    # Add a search box for quick lookups by title or author
    search_fields = ("title", "author")

    # Filter sidebar to narrow down by publication year
    list_filter = ("publication_year",)

    # Optional UX improvements
    ordering = ("-publication_year", "title")
    list_per_page = 25

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # Add your custom fields to the admin display
    # This copies the default UserAdmin fieldsets and adds a new one
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    # This adds the custom fields to the 'add user' form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    # This adds the fields to the user list display
    list_display = UserAdmin.list_display + ('date_of_birth', 'profile_photo')

# Register your new admin
admin.site.register(CustomUser, CustomUserAdmin)