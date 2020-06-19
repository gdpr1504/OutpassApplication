from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

DEPT_CHOICES= [
    ('it', 'IT'),
    ('cse', 'CSE'),
    ('civil', 'CIVIL'),
    ('eee', 'EEE'),
    ('ece','ECE'),
    ('chemical','CHEMICAL'),
    ('biotech','BIOTECH'),
    ('mech','MECH'),
    ('prod','PROD'),
    ]



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Put in a valid email address.')
    phone_number = forms.CharField(max_length=10, required=False, help_text='Required.')
    Department= forms.CharField(widget=forms.Select(choices=DEPT_CHOICES))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'Department','phone_number', 'email', 'password1', 'password2', )