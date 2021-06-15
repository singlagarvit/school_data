from django.urls import path
from .views import analytics, get_data

urlpatterns = [
	path('', analytics, name='analytics'),
	path('get-data/', get_data, name='get_data'),
]