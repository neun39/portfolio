from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['date', 'title', 'content']
        labels = {
            'date':'日付',
            'title':'タイトル',
            'content':'内容',
        }
        