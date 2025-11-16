# Advanced Features and Security Project

This project implements advanced Django features, including custom user models, permissions, and security best practices.

## Task 1: Permissions and Groups

This project uses custom permissions on the `Book` model to control user actions.

### Permissions Defined
- **`can_create`**: Allows creating a new book.
- **`can_view`**: Allows viewing book details.
- **`can_edit`**: Allows editing an existing book.
- **`can_delete`**: Allows deleting a book.

These permissions are defined in `relationship_app/models.py` in the `Book` model's `Meta` class.

### Groups Configured
Permissions are assigned to users via groups in the Django admin:
- **Viewers**: Has the `can_view` permission.
- **Editors**: Has `can_create`, `can_view`, and `can_edit` permissions.
- **Admins**: Has all four permissions.

### View Enforcement
Views in `relationship_app/views.py` use the `@permission_required` decorator to enforce these rules.