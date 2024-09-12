from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField()

#     def __str__(self):
#         return self.user.username
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment_date = models.DateField()

    def __str__(self):
        return self.name
    
class Course(models.Model):
    title = models.CharField(max_length=100)   
    students = models.ManyToManyField(Student, related_name="courses") 

    def __str__(self):
        return self.title