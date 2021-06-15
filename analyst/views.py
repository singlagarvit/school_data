from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import user_passes_test
from data.models import User, Student

import datetime

def analytics(request):
	return render(request, 'analytics.html')

def get_data(request):
	labels = [datetime.date.today()	- datetime.timedelta(days=i) for i in range(0, 10)]
	default_items = []
	for l in labels:
		default_items.append(Student.objects.filter(completed_on__date=l, complete=True).count())
	data = {
		"labels": labels,
		"default": default_items,
	}
	return JsonResponse(data)