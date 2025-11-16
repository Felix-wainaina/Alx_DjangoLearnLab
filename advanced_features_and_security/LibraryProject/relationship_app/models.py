# relationship_app/models.py
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth import get_user_model

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    publication_year = models.IntegerField(default=2000)  # <-- ADD THIS LINE

    def __str__(self):
        return f"{self.title} (by {self.author.name})"
    # --- ADD THIS META CLASS ---
    class Meta:
        # Documentation for permissions (Task 1, Step 5)
        # Custom permissions are defined here to control access
        # based on user groups (Editors, Viewers, Admins).
        # These are checked in relationship_app/views.py
        permissions = [
            ("can_create_book", "Can create book"),
            ("can_view_book", "Can view book"),
            ("can_edit_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]

class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(
        Book,
        related_name='libraries',
        blank=True
    )

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name='librarian'
    )

    def __str__(self):
        return f"{self.name} — {self.library.name}"
    
    # --- ADD THIS NEW MODEL AND SIGNAL AT THE BOTTOM ---

# Step 1: Extend the User Model
class UserProfile(models.Model):
    # Link to the built-in User model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Role choices
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    
    # Role field
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Automatic Creation: Django Signal
# This function will run *after* a User object is saved
@receiver(post_save)
def create_user_profile(sender, instance, created, **kwargs):
    # only act for the active user model
    UserModel = get_user_model()
    if isinstance(instance, UserModel) and created:
        UserProfile.objects.create(user=instance)

# This second signal ensures the profile is saved when the user is saved
@receiver(post_save)
def save_user_profile(sender, instance, **kwargs):
    UserModel = get_user_model()
    if isinstance(instance, UserModel):
        # avoid error if profile missing for any reason
        try:
            instance.userprofile.save()
        except UserProfile.DoesNotExist:
            pass
