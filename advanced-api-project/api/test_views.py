# api/test_views.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author
from datetime import date

class BookAPITests(APITestCase):
    """
    Test suite for the Book API.
    Covers: CRUD operations, Permissions, Filtering, Searching, and Ordering.
    """

    def setUp(self):
        """
        Set up the test environment:
        1. Create a test user (for authentication).
        2. Create test data (Author and Books).
        3. Define URLs.
        """
        # Create a user for authentication tests
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create an author
        self.author = Author.objects.create(name="J.K. Rowling")

        # Create books
        self.book1 = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Harry Potter and the Chamber of Secrets",
            publication_year=1998,
            author=self.author
        )

        # Define URLs using reverse() to keep tests dynamic
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        # specific book URLs
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book1.pk})

    # --- CRUD & PERMISSION TESTS ---

    def test_list_books_unauthenticated(self):
        """Ensure unauthenticated users can view the book list."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # We created 2 books in setUp

    def test_detail_book_unauthenticated(self):
        """Ensure unauthenticated users can view a single book detail."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated(self):
        """Ensure logged-in users can create a book."""
        self.client.login(username='testuser', password='password123')
        data = {
            'title': 'Harry Potter and the Prisoner of Azkaban',
            'publication_year': 1999,
            'author': self.author.pk
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated users CANNOT create a book."""
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2022,
            'author': self.author.pk
        }
        response = self.client.post(self.create_url, data)
        # Should be 403 Forbidden (or 401 Unauthorized depending on settings)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_update_book_authenticated(self):
        """Ensure logged-in users can update a book."""
        self.client.login(username='testuser', password='password123')
        data = {
            'title': 'Updated Title',
            'publication_year': 1997,
            'author': self.author.pk
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book_authenticated(self):
        """Ensure logged-in users can delete a book."""
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # --- ADVANCED QUERY TESTS (Filtering, Searching, Ordering) ---

    def test_filter_books_by_year(self):
        """Test filtering by publication_year."""
        # Filter for the year 1998 (Book 2)
        response = self.client.get(self.list_url, {'publication_year': 1998})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book2.title)

    def test_search_books(self):
        """Test searching by title."""
        # Search for "Chamber" (Should match Book 2)
        response = self.client.get(self.list_url, {'search': 'Chamber'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book2.title)

    def test_order_books(self):
        """Test ordering by publication_year."""
        # Order descending (newest first)
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # First item should be Book 2 (1998), Second item Book 1 (1997)
        self.assertEqual(response.data[0]['title'], self.book2.title)
        self.assertEqual(response.data[1]['title'], self.book1.title)

    # --- VALIDATION TEST ---

    def test_future_publication_year(self):
        """Ensure we cannot create a book with a future year."""
        self.client.login(username='testuser', password='password123')
        future_year = date.today().year + 5
        data = {
            'title': 'Future Book',
            'publication_year': future_year,
            'author': self.author.pk
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)