from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import validate_marks

class Student(models.Model):
	school = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	rollno = models.CharField(max_length=11)
	regno = models.CharField(max_length=11)
	fname = models.CharField(max_length=40)
	dob = models.DateField()
	sub1 = models.IntegerField()
	sub2 = models.IntegerField()
	sub3 = models.IntegerField(null=True, blank=True)
	math = models.CharField(max_length=2, null=True, blank=True, validators=[validate_marks])
	english = models.CharField(max_length=2, null=True, blank=True, validators=[validate_marks])
	hindi = models.CharField(max_length=2, null=True, blank=True, validators=[validate_marks])
	complete = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.school.username} - {self.rollno}'

	def get_absolute_url(self):
		return reverse('student', kwargs={
				'rollno': self.rollno
			})

	class Meta:
		permissions = [
			("can_update", "Can update the data of students"),
			("can_change_password", "Can change the password of school user"),
		]

class SchoolProfile(models.Model):
	school = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=70)
	phone = models.BigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
	created_on = models.DateTimeField(auto_now_add=True)
	modified_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.school.username