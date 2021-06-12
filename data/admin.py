from django.contrib import admin
from .models import Student, SchoolProfile

class SchoolProfileAdmin(admin.ModelAdmin):
	list_display = ['school', 'name', 'email', 'phone', 'created_on', 'modified_on']

admin.site.register(Student)
admin.site.register(SchoolProfile, SchoolProfileAdmin)