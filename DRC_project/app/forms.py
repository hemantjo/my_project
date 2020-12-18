from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from . import models

class SigninForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["email"]

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]