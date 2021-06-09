from django import forms
from .models import Student

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
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control mb-3'})
			if self[field].value() is not None:
				self.fields[field].widget.attrs.update({'disabled': ''})
			self.fields['math'].label = SUBJECT_CODE_DICT[self['sub1'].value()].title() #'math' => 'fl'
			self.fields['english'].label = SUBJECT_CODE_DICT[self['sub2'].value()].title() #'english' => second field
			self.fields['hindi'].label = SUBJECT_CODE_DICT[self['sub3'].value()].title() #'hindi' => third field
