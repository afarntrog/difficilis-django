from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField(required=False)
    password2 = None

    class Meta:
        model = User # When ever this form validates then it'll create a new user
        fields = ['username', 'password1'] # Add 'password2' for validation and then add 'email' if you want a email    


class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username']