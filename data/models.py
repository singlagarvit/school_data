from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
	school = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	rollno = models.CharField(max_length=11)
	regno = models.CharField(max_length=11)
	fname = models.CharField(max_length=40)
	dob = models.DateField()
	math = models.CharField(max_length=2)

	def __str__(self):
		return f'{self.school.username} - {self.rollno}'