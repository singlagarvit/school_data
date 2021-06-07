from django.urls import path
from .views import index, students, student

urlpatterns = [
	path('', index, name='index'),
	path('students/', students, name='students'),
	path('student/<rollno>/', student, name='student'),
]