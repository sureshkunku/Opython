from django.apps import AppConfig
from django import forms
from django.contrib.auth.models import User

from Opythonapp.models import UserProfile

class OpythonappConfig(AppConfig):
    name = 'Opythonapp'

class UserProfileCreation(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('username','password','first_name','last_name','email','is_superuser','gender','cell','address')

