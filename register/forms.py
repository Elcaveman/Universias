from django import forms
from .models import User , Profile
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    pass

class UserExtrasForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profil_pic','domaine','bio')