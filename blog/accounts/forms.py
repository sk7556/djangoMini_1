from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input-class'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-input-class'}))
    
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input-class'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-input-class'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-input-class'}))