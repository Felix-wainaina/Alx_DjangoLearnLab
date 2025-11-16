# Advanced Features and Security Project

This project implements advanced Django features, including custom user models, permissions, and security best practices.

## Task 1: Permissions and Groups

This project uses custom permissions on the `Book` model to control user actions.

### Permissions Defined
- **`can_create`**: Allows creating a new book.
- **`can_view`**: Allows viewing book details.
- **`can_edit`**: Allows editing an existing book.
- **`can_delete`**: Allows deleting a book.

These permissions are defined in `bookshelf/models.py` in the `Book` model's `Meta` class.

### Groups Configured
Permissions are assigned to users via groups in the Django admin:
- **Viewers**: Has the `can_view` permission.
- **Editors**: Has `can_create`, `can_view`, and `can_edit` permissions.
- **Admins**: Has all four permissions.

### View Enforcement
Views in `bookshelf/views.py` use the `@permission_required` decorator to enforce these rules.

## Task 2: Implementing Security Best Practices

This project implements several security measures.

- **Secure Settings**: `settings.py` is configured with `SECURE_CONTENT_TYPE_NOSNIFF`, `X_FRAME_OPTIONS`, and other settings. `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` are set to `False` for HTTP development but should be `True` in production.
- **CSRF Protection**: All `POST` forms in the project (like the admin) are protected. The search form in `form_example.html` uses `GET`, but a commented example shows how `{% csrf_token %}` is used for `POST` forms.
- **SQL Injection Prevention**: The `search_books` view in `bookshelf/views.py` uses a Django `SearchForm` to validate and sanitize user input. The view uses the Django ORM's `filter()` method, which parameterizes queries and prevents SQL injection.
- **Content Security Policy (CSP)**: `django-csp` is installed and configured in `settings.py` to restrict content sources, mitigating XSS risks.

## Task 3: HTTPS and Secure Redirects (Security Review)

This project is configured to enforce production-level web security.

- **HTTPS Enforcement**: When `DEBUG = False`, `SECURE_SSL_REDIRECT` is set to `True`, forcing all user traffic over HTTPS.
- **HSTS (HTTP Strict Transport Security)**: `SECURE_HSTS_SECONDS` is set for one year, which, along with `includeSubDomains` and `preload`, instructs browsers to *only* communicate with this site via HTTPS, protecting against man-in-the-middle attacks.
- **Secure Cookies**: `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` are set to `True` in production, ensuring that session and CSRF tokens are never transmitted over insecure HTTP.
- **Deployment**: The `DEPLOYMENT.md` file contains a sample Nginx configuration for SSL/TLS termination, which complements Django's security settings.