from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude = ['complete']

	def __init__(self, *args, **kwargs):
		super(StudentForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control mb-3'})
			if self[field].value() is not None:
				self.fields[field].widget.attrs.update({'disabled': ''})
