from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Put in a valid email address.')
    Department = forms.CharField(max_length=5, required=False, help_text='Required.')
    phone_number = forms.CharField(max_length=10, required=False, help_text='Required.')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'Department','phone_number', 'email', 'password1', 'password2', )