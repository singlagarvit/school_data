from django import forms
from .models import Student, SchoolProfile

SUBJECT_CODE_DICT = {
	1:'english',
	2:'hindi',
	3:'punjabi',
	4:'python',
	5:'java',
	6:'Sanskrit'
}

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude = ['complete']

	def __init__(self, *args, **kwargs):
		super(StudentForm, self).__init__(*args, **kwargs)
		fields = self.fields.copy()
		fields.pop('sub3')
		fields.pop('hindi')
		self.fields['hindi'].widget.attrs.update({'class': 'form-control mb-3', 'required': ''})
		if self['sub3'].value() is not None:
			try:
				self.fields['hindi'].label = SUBJECT_CODE_DICT[int(self['sub3'].value())].title() #'hindi' => third field
			except:
				self.fields['hindi'].label = 'No Subject' #'hindi' => third field
				self.fields['hindi'].widget.attrs.update({'disabled': ''})
				self.fields['hindi'].widget.attrs.pop('required')
		else:
			print('else')
			self.fields['hindi'].label = 'No Subject' #'hindi' => third field
			self.fields['hindi'].widget.attrs.update({'disabled': ''})
			self.fields['hindi'].widget.attrs.pop('required')
		for field in fields:
			self.fields[field].widget.attrs.update({'class': 'form-control mb-3', 'required': ''})
			if self[field].value() is not None:
				self.fields[field].widget.attrs.update({'disabled': ''})
			self.fields['math'].label = SUBJECT_CODE_DICT[int(self['sub1'].value())].title() #'math' => 'fl'
			self.fields['english'].label = SUBJECT_CODE_DICT[int(self['sub2'].value())].title() #'english' => second field
			if len(self[field].errors) > 0:
				self.fields[field].widget.attrs.pop('disabled')
		
class SchoolProfileForm(forms.ModelForm):
	class Meta:
		model = SchoolProfile
		exclude = ['school']