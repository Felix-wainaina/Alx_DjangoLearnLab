from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

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