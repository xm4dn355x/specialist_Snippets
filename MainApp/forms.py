from django.forms import ModelForm, TextInput, ChoiceField
from .models import Snippet


LANG_CHOICES = (
    ('py', 'Python'),
    ('js', 'JavaScript'),
    ('cpp', 'C++')
)


class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code']
       widgets = {
           'name': TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Название сниппета'}),
       }
