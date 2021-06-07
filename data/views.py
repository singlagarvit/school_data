from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Student

import csv

def index(request):
	return HttpResponse('<a href="/student/">Student</a>')

def student(request):
	with open(f"{settings.BASE_DIR}\\students.csv", "r") as csv_file:
		csv_reader = csv.reader(csv_file)
		next(csv_reader)
		for line in csv_reader:
			student = Student.objects.create(school_id=line[0], rollno=line[1], regno=line[2], fname=line[3], dob=line[4], math=line[5])
	return HttpResponse('Student Accounts Updated')