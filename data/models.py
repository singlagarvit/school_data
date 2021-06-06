from django.db import models

class School(models.Model):
	index = models.CharField(max_length=10, unique=True)
	name = models.CharField(max_length=120)
	email = models.EmailField(max_length=150)
	phone = models.CharField(max_length=10)

	def __str__(self):
		return self.index