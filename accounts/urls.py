from django.urls import path  
from . import views 
urlpatterns = [
	path('doctors/', views.index, name='index'),
	path('login/', views.user_login, name='login'),
	path('signup/', views.signup, name='signup'),
	path('myprofile/', views.myprofile, name='myprofile'),
	path('update_profile/', views.update_profile, name='update_profile'),
	path('profile/<slug:slug>/', views.doctor_profile, name='doctor_profile'),
]
