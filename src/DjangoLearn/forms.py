from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserForm(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label="password", max_length=100)
    type = forms.ChoiceField(choices=[('teacher', 'Teacher'), ('student', 'Student')])

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Invalid username or password',
    }

class CourseForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    description = forms.CharField(label="description", max_length=100)