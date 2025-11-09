# relationship_app/query_samples.py
import os
import django

# IMPORTANT: this must match the folder that contains settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def prepare_sample_data():
    # Create authors and books idempotently
    author, _ = Author.objects.get_or_create(name="Jane Doe")
    b1, _ = Book.objects.get_or_create(title="Django Uncovered", author=author)
    b2, _ = Book.objects.get_or_create(title="Advanced Django", author=author)

    a2, _ = Author.objects.get_or_create(name="John Smith")
    b3, _ = Book.objects.get_or_create(title="Python Basics", author=a2)

    # Library and add books (ManyToMany)
    lib, created = Library.objects.get_or_create(name="Central Library")
    # add returns nothing, so ensure we add only if not already present
    lib.books.add(b1, b3)

    # OneToOne: create librarian only if not exists
    if not hasattr(lib, 'librarian'):
        Librarian.objects.create(name="Mary the Librarian", library=lib)

    return {
        'author': author,
        'b1': b1,
        'b2': b2,
        'b3': b3,
        'library': lib
    }

def run_queries(samples):
    author = samples['author']
    library = samples['library']

    print("\n--- Sample data created ---")
    print("Author:", author)
    print("Library:", library)
    print("Books in DB:", Book.objects.count())

    # 1) Query all books by a specific author
    books_by_author = Book.objects.filter(author=author)
    print(f"\nBooks by {author.name}:")
    for b in books_by_author:
        print(" -", b.title)

    # 2) List all books in a library (ManyToMany)
    print(f"\nBooks in library '{library.name}':")
    for b in library.books.all():
        print(" -", b.title)

    # 3) Retrieve the librarian for a library (OneToOne)
    try:
        librarian = library.librarian
        print(f"\nLibrarian for {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian set for {library.name}")

if __name__ == "__main__":
    samples = prepare_sample_data()
    run_queries(samples)
