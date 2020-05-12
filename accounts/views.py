from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .models import Profile 
from .forms import LoginForm ,UserRegisterationForm, UpdateUserForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import  login_required
# Create your views here.
def index(request):
	doctors = Profile.objects.all()
	context = {
		'doctors' : doctors,
	}
	return render(request, 'index.html', context)

def doctor_profile(request, slug):
	doctor = Profile.objects.get(slug=slug)
	context = {
		'doctor': doctor,
	}
	return render(request, 'accounts/doctor_profile.html', context)

def user_login(request):	
	if request.method == 'POST':
		form = LoginForm() 
		username = request.POST.get('username')
		password = request.POST.get('password')
		user =  authenticate(request, username=username, password=password)
		if  user is not None:
			login(request, user)
			return redirect('myprofile')
	else:
		form = LoginForm() 
	return render(request, 'accounts/login.html', {'form': form})

######## User Registeration 
def signup(request):
	if request.method == 'POST':
		form = UserRegisterationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user =  authenticate(request, username=username, password=password)
			login(request, user)
			return redirect('myprofile')
	else:
		form = UserRegisterationForm()

	return render(request, 'accounts/signup.html',{'form':form})

@login_required()
def myprofile(request):
	return render(request, 'accounts/myprofile.html',{})

def update_profile(request):
	user_form = UpdateUserForm(instance=request.user)
	if request.method == 'POST':
		user_form = UpdateUserForm(request.POST, instance=request.user)
		if user_form.is_valid():
			user_form.save()
			return redirect('index')
	# else:
	# 	user_form = UpdateUserForm(instance=request.user)

	return render(request, 'accounts/update_profile.html',{'user_form':user_form})