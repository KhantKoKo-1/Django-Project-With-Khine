from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
     path('authors/create/', views.author_create, name='author_create'),
    path('authors/<int:pk>/update/', views.author_update, name='author_update'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),
    path('books/', views.book_list, name='book_list'),
    path('students/', views.student_list, name='student_list'),
    path('courses/', views.course_list, name='course_list'),
]
