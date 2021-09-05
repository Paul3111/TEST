from django import forms
from .models import Topic, Entry, UserInformation


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class UserInformationForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = '__all__'

