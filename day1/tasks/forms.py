from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields =['title','description']
        labels = {
            "title" : "タイトル",
            "description" : "説明",
        }

class TaskToggleCompleteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['completed'] 