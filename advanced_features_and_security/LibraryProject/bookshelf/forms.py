from django import forms

# --- RENAME THIS CLASS ---
class ExampleForm(forms.Form):
    # Documentation (Task 2, Step 3):
    # This form validates user input.
    query = forms.CharField(label='Search for a book title', max_length=100)