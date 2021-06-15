from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as user_login, logout as user_logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.conf import settings
from django.core.mail import send_mail
# from mailer import send_mail

from .models import Student, User
from .forms import StudentForm, SchoolProfileForm
from .decorators import has_update_permission, has_password_change_permission
from .tokens import account_activation_token

import csv

@login_required
@has_update_permission
def index(request):
	return HttpResponse(f'<a href="/students/">{ request.user }  Students List</a>')

@login_required
@has_update_permission
def students(request):
	all_students = Student.objects.filter(school=request.user).order_by('rollno')
	paginator = Paginator(all_students, 1)
	page_number = request.GET.get('page')
	try:
		students = paginator.get_page(page_number)
	except (EmptyPage, InvalidPage):
		students = paginator.get_page(1)

	index = students.number - 1
	max_index = len(paginator.page_range)
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index else max_index
	page_range = paginator.page_range[start_index:end_index]

	try:
		first_student = all_students.filter(complete=False)[0]
	except:
		first_student = None

	context = {
		'students': students,
		'first_student': first_student,
		'page_range': page_range
	}
	return render(request, 'student_list.html', context)

@login_required
@has_update_permission
def student(request, rollno):
	last_elements_list = ['6', '5', '4', '3', '2', '1']
	students = Student.objects.filter(school=request.user).order_by('rollno')
	student = Student.objects.get(rollno=rollno, school=request.user)
	form = StudentForm(instance=student)

	if request.method == 'POST':
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.complete = True
			obj.save()
			pass

			try:
				next_student = students.filter(rollno__gt=rollno, complete=False)[0]
				messages.success(request, f'Congratulations! Data for student {obj.rollno} have been updated.')
				return redirect(next_student.get_absolute_url())
			except IndexError:
				messages.success(request, 'Congratulations! Data for all the students have been updated.')
				return redirect('students')

	context = {
		'student': student,
		'students': students,
		'form': form,
		'last_elements_list': 'last_elements_list'
	}
	return render(request, 'student.html', context)

@login_required
def school_profile(request):
	try:
		profile = request.user.schoolprofile
		return redirect('index')
	except:
		pass
	user = request.user
	form = SchoolProfileForm()
	if request.method == 'POST':
		form = SchoolProfileForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.school = user
			profile.save()
			user.email = profile.email
			user.save()
			return redirect('change_password')
	context = {
		'form': form
	}
	return render(request, 'school-profile.html', context)

@login_required
def change_password(request):
	current_site = get_current_site(request)
	mail_subject = "Activate your account"
	message = render_to_string('account_activation_email.html', {
		'user': request.user,
		'domain': current_site.domain,
		'uid': urlsafe_base64_encode(force_bytes(request.user.pk)),
		'token': account_activation_token.make_token(request.user),
	})
	send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [request.user.email])
	context = {
		'user': request.user
	}
	return render(request, 'change-password.html', context)

@login_required
def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid) 
	except:
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		if request.user == user:
			permission = Permission.objects.get(codename='can_change_password')
			request.user.user_permissions.add(permission)
			return redirect('reset_password')
	return HttpResponse('Activation Link Invalid')

@login_required
@has_password_change_permission
def reset_password(request):
	form = PasswordChangeForm(request.user)
	update_permission = Permission.objects.get(codename='can_update')
	password_change_permission = Permission.objects.get(codename='can_change_password')
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			password = form.save()
			update_session_auth_hash(request, password)
			if not request.user.has_perm('data.can_update'):
				request.user.user_permissions.add(update_permission)
			request.user.user_permissions.remove(password_change_permission)
			return redirect('index')
	context = {
		'form': form
	}
	return render(request, 'reset-password.html', context)

@login_required
def logout(request):
	user_logout(request)
	return redirect('index')