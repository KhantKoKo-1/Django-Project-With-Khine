from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AuthorForm
from .models import Author, Book, Student, Course
# Create your views here.

def home (request):
    # context = {}
    return render(request, 'index.html')

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
        else:
            print(form.errors)  # This will help debug if validation errors are being raised

    else:
        form = AuthorForm()

    return render(request, 'author_form.html', {'form': form, 'action': 'Create'})

def student_list(request):
    return render(request, 'student_list.html')

def book_list(request):
    return render(request, 'book_list.html')

def course_list(request):
    return render(request, 'course_list.html')