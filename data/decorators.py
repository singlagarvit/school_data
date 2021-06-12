from django.shortcuts import redirect

def has_update_permission(func):
	def wrap(request, *args, **kwargs):
		if request.user.has_perm('data.can_update'): #data => app_name
			return func(request, *args, **kwargs)
		else:
			return redirect('school_profile')
	return wrap

def has_password_change_permission(func):
	def wrap(request, *args, **kwargs):
		if request.user.has_perm('data.can_change_password'):
			return func(request, *args, **kwargs)
		else:
			return redirect('change_password')
	return wrap