from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(label='كلمة المرور ', widget= forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')

# class  UserRegisterationForm(forms.ModelForm):
#     username = forms.CharField(label="اسم المستخدم ", max_length=20)
#     password = forms.CharField(label=" كلمة المرور ", min_length=8 ,widget= forms.PasswordInput())
#     class Meta:
#         model = User
#         fields = ("username","password")

class  UserRegisterationForm(UserCreationForm):
    username = forms.CharField(label="اسم المستخدم ", max_length=20)
    first_name = forms.CharField(label="الاسم الاول ", max_length=20)
    last_name = forms.CharField(label="الاسم الاخير ", max_length=20)
    email = forms.EmailField(label=" البريد الالكتروني" , required=True)
    password1 = forms.CharField(label=" كلمة المرور ", min_length=8 ,widget= forms.PasswordInput())
    password2 = forms.CharField(label=" تأكيد كلمة المرور ", min_length=8 ,widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "first_name","last_name","email","password1","password2")


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label="الاسم الاول ")
    last_name = forms.CharField(label="الاسم الاخير ")
    email = forms.EmailField(label=" البريد الالكتروني" )
    class Meta:
        model = User
        fields = ('first_name','last_name','email')