from django import forms
from .models import Task


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'