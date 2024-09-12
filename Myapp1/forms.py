from django import forms
from .models import Author
from django.core.exceptions import ValidationError

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birthdate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    # Make both fields not required in the form
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}), required=False)
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError("Custom Error: Name is required.")  # Custom error message for name
        return name

    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')
        if not birthdate:
            raise ValidationError("Custom Error: Birthdate is required.")  # Custom error message for birthdate
        return birthdate
