from django import forms
from .models import Topic, Entry, UserInformation, CustomerMessage, LoanApplication, LoanCalculation


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
        # fields = '__all__'
        fields = ('customer_message_subject', 'customer_message')
        labels = {'customer_message_subject': 'Subject', 'customer_message': 'Message'}
        widgets = {'customer_message_subject': forms.Textarea(attrs={'cols': 60, 'rows': 1}),
                   'customer_message': forms.Textarea(attrs={'cols': 60, 'rows': 5})}


class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ('loan_purpose', 'loan_amount', 'loan_term', 'interest_rate', 'date_of_birth', 'marital_status',
                  'children', 'residential_status', 'residence_duration', 'employment_status', 'monthly_salary',
                  'monthly_expenses', 'monthly_rent', 'bankrupted', 'loan_documentation')
        labels = {'loan_purpose': 'Loan purpose', 'loan_amount': 'Loan amount', 'loan_term': 'Loan term (years)',
                  'interest_rate': 'Interest rate', 'date_of_birth': 'Date of Birth (dd/mm/yyyy)',
                  'marital_status': 'Marital status', 'Children': 'No. of children',
                  'residential_status': 'Residential status', 'residence_duration': 'Years lived at current address',
                  'employment_status': 'Employment status', 'monthly_salary': 'Monthly salary',
                  'monthly_expenses': 'Monthly expenses', 'monthly_rent': 'Monthly rent',
                  'bankrupted': 'Are you currently bankrupted?', 'loan_documentation': 'Upload scanned documentation'}


class LoanCalculationForm(forms.ModelForm):
    class Meta:
        model = LoanCalculation
        # fields = ('principal', 'interest_rate', 'duration', 'monthly_payment')
        fields = ('principal', 'interest_rate', 'duration')
        labels = {'principal': 'Loan amount', 'interest_rate': 'Interest rate', 'duration': 'Loan term (years)'}
