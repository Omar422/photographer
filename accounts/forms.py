from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm, TextInput, EmailInput

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : TextInput(attrs = {'id':'signupId','placeholder':'اسم المستخدم (سوف يتم استعماله لتسجيل الدخول)'}),
            'email' : EmailInput(attrs={'placeholder':'البريد الإلكتروني'}),
            
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name'    : TextInput(attrs={'class':'form-control'}),
            'last_name'    : TextInput(attrs={'class':'form-control'})
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = 'user', 'user_slug'
        widgets = {
            'user_phone'    : TextInput(attrs={'class':'form-control'}),
            'user_address'    : TextInput(attrs={'class':'form-control'})
        }
