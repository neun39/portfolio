from django import forms
from .models import Task

class TaskForm(forms.Form):
    class Meta:
        model = Task
        fields =['fields','description']

class TaskToggleCompleteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['completed'] 