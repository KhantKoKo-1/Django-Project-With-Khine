from django import forms
from .models import UserProfile, Author, Book, Student, Course

# Form for UserProfile (One-to-One Relationship)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']

# Form for Author (One-to-Many Relationship)
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birthdate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

# Form for Book (One-to-Many Relationship)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'published_date', 'author']

# Form for Student (Many-to-Many Relationship)
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'enrollment_date']

# Form for Course (Many-to-Many Relationship)
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'students']  # Many-to-many field
        widgets = {
            'students': forms.CheckboxSelectMultiple(),  # Allows selecting multiple students
        }
