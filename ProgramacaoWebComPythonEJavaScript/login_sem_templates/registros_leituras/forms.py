from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':'texto'}
        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Digite o tópico aqui...',
                'autofocus': 'autofocus',
                'maxlength': 100, 
                'minlength': 5            
            }),
        }

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Digite suas anotações',
                'cools':80
            })
        }

