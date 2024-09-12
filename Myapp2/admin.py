from django.contrib import admin
from .models import UserProfile, Author, Book, Student, Course

admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Course)
