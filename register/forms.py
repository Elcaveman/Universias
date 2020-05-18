from django import forms
from .models import User , Profile
from django.contrib.auth.forms import UserCreationForm , UsernameField

class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.

    """
    username = UsernameField(widget=forms.TextInput(attrs={
        'class':"input100",
        'name':"email",
        'placeholder':"Username",
        'autofocus': True
        }))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class':"input100",
            'name':"pass",
            'placeholder':"Password",
            'autocomplete': 'current-password'}),
    )

#? UserCreationForm is also used

class UserForm(forms.ModelForm):
    # <input class="input100" type="password" name="pass" placeholder="Password">
    # <input class="input100" type="text" name="email" placeholder="Email">
    # using JS to set classes for now need to read django source code for form_classes :/
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class UserExtrasForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profil_pic','domaine','bio')

