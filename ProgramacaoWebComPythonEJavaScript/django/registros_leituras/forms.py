from django import forms
from .models import Topic

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