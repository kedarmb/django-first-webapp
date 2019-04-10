from django import forms
from django.contrib.auth.forms import UserCreationForm


# Inheriting UserCreationClass to SignupForm Class
class SignupForm(UserCreationForm):
    email = forms.EmailField()

# Inheriting Form class from forms modules
class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)