from django.contrib import admin
from .models import Student, SchoolProfile, User

class SchoolProfileAdmin(admin.ModelAdmin):
	list_display = ['school', 'name', 'email', 'phone', 'created_on', 'modified_on']

class StudentAdmin(admin.ModelAdmin):
	list_display = ['school', 'rollno', 'fname', 'dob', 'completed_on']

admin.site.register(Student, StudentAdmin)
admin.site.register(User)
admin.site.register(SchoolProfile, SchoolProfileAdmin)