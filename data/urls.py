from django.urls import path
from django.contrib.auth.views import LoginView
from .views import index, students, student, change_password, school_profile, logout, activate, reset_password

urlpatterns = [
	path('', index, name='index'),
	path('login/', LoginView.as_view(template_name='login.html')),
	path('logout/', logout, name='logout'),
	path('students/', students, name='students'),
	path('update-school-profile/', school_profile, name='school_profile'),
	path('change-password/', change_password, name='change_password'),
	path('reset-password/', reset_password, name='reset_password'),
	path('student/<rollno>/', student, name='student'),
	path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]