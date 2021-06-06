from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.hashers import make_password
from .models import School

import csv

def index(request):
	response = HttpResponse(content_type='text/csv')
	password = 'password'
	hash_password = make_password(password)

	with open(f"{settings.BASE_DIR}\\schools.csv", "r") as csv_file:
		csv_reader = csv.reader(csv_file)
		next(csv_reader)
		writer = csv.writer(response)
		writer.writerow(['School Index', 'School Name', 'Email', 'Phone', 'Password', 'Password Hash'])
		for line in csv_reader:
			line.extend([password, hash_password])
			writer.writerow(line)
	response['Content-Disposition'] = 'attachment;filename="school_users.csv"'

	return response