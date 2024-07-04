from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ["email", "password1"]


class Login_form(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username","email", "password"]