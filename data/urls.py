from django.urls import path
from .views import index, student

urlpatterns = [
	path('', index),
	path('student/', student),
]