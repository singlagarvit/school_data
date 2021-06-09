from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Student(models.Model):
	school = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	rollno = models.CharField(max_length=11)
	regno = models.CharField(max_length=11)
	fname = models.CharField(max_length=40)
	dob = models.DateField()
	sub1 = models.IntegerField()
	sub2 = models.IntegerField()
	sub3 = models.IntegerField()
	math = models.CharField(max_length=2, null=True, blank=True)
	english = models.CharField(max_length=2, null=True, blank=True)
	hindi = models.CharField(max_length=2, null=True, blank=True)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.school.username} - {self.rollno}'

	def get_absolute_url(self):
		return reverse('student', kwargs={
				'rollno': self.rollno
			})