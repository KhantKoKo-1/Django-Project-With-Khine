from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book, Student, Course
from .forms import AuthorForm

# List of Authors
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

# Create Author
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form, 'action': 'Create'})

# Update Author
def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_form.html', {'form': form, 'action': 'Update'})

# Delete Author
def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'author_confirm_delete.html', {'author': author})

# List of Books
def book_list(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'book_list.html', {'books': books})

# List of Students
def student_list(request):
    students = Student.objects.prefetch_related('courses').all()
    return render(request, 'student_list.html', {'students': students})

# List of Courses
def course_list(request):
    courses = Course.objects.prefetch_related('students').all()
    return render(request, 'course_list.html', {'courses': courses})
