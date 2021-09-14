from django import forms
from .models import Topic, Entry, UserInformation, CustomerMessage


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
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email', 'contact_number', 'address_line1',
                  'address_line2', 'address_line3', 'address_city', 'address_post_code',
                  'address_country', 'alerts', 'newsletter', 'address_country', 'profile_picture',)


class CustomerMessageForm(forms.ModelForm):
    class Meta:
        model = CustomerMessage
        fields = '__all__'
