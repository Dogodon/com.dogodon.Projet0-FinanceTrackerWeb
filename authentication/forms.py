# authentication/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=False)
    birthdate = forms.DateField(required=False)

    class Meta:
        model = CustomUser
        fields = ("username", "full_name", "birthdate", "password1", "password2")
