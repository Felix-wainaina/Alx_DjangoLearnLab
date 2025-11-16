from django import forms

class SearchForm(forms.Form):
    # Documentation (Task 2, Step 3):
    # This form validates user input.
    # Using CharField (max_length=100) helps sanitize the
    # input and prevent overly large or malicious data.
    query = forms.CharField(label='Search for a book title', max_length=100)