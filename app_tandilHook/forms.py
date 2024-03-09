from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Lure, Cloth, Tool

class LureForm(forms.ModelForm):
    class Meta:
        model = Lure
        fields = '__all__'

class ClothForm(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = '__all__'

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
