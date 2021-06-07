from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm

import csv

def index(request):
	return HttpResponse('<a href="/students/">Students List</a>')

@login_required
def students(request):
	students = Student.objects.filter(school=request.user).order_by('rollno')
	try:
		first_student = students.filter(complete=False)[0]
	except:
		first_student = None
	context = {
		'students': students,
		'first_student': first_student
	}
	return render(request, 'student_list.html', context)

@login_required
def student(request, rollno):
	students = Student.objects.filter(school=request.user).order_by('rollno')
	student = Student.objects.get(rollno=rollno, school=request.user)
	form = StudentForm(instance=student)

	if request.method == 'POST':
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.complete = True
			obj.save()

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
		'form': form
	}
	return render(request, 'student.html', context)