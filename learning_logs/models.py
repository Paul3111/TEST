from django.db import models
from django import forms
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
from django.core.validators import MinValueValidator, MaxValueValidator


class Topic(models.Model):
    """ A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return f" {self.text}"


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."


class UserInformation(models.Model):
    """User information"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    contact_number = PhoneNumberField(unique=True, null=False, blank=False)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50, blank=True)
    address_line3 = models.CharField(max_length=50, blank=True)
    address_city = models.CharField(max_length=50)
    address_county = models.CharField(max_length=50)
    address_post_code = models.CharField(max_length=50)
    address_country = models.CharField(max_length=50)
    alerts = models.BooleanField(default=False)
    newsletter = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='media', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "InfoUsers"

    def __str__(self):
        """To display these fields in the admin panel and make them available for html template"""
        return f"{self.first_name} {self.last_name} - {self.email}. Added on: {self.date_created} {self.owner}"


class CustomerMessage(models.Model):
    """Table to store customer messages"""
    customer_message_subject = models.TextField(max_length=200)
    customer_message = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.customer_message_subject[:50]} {self.date_added})"


purpose_list = (('Home improvements', 'Home improvements'), ('Debt consolidation', 'Debt consolidation'),
                ('Car purchase', 'Car purchase'), ('Holiday', 'Holiday'), ('Wedding', 'Wedding'),
                ('Buy property', 'Buy property'), ('Buy land', 'Buy land'),
                ('Buy property with land', 'Buy property with land'), ('Other', 'Other'),)

term_list = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'))

marital_list = (('Married', 'Married'), ('Divorced', 'Divorced'), ('Single', 'Single'),
                ('Co-habituating', 'Co-habituating'), ('Widowed', 'Widowed'),
                ('Civil Partnership', 'Civil Partnership'), ('Separated', 'Separated'))

residential_status_list = (('Owner', 'Owner'), ('Owner with mortgage', 'Owner with mortgage'), ('Tenant', 'Tenant'),
                           ('Council tenant', 'Council tenant'), ('Employer accommodation', 'Employer accommodation'),
                           ('Living with family or friends', 'Living with family or friends'))

employment_status_list = (('Full time', 'Full time'), ('Self employed', 'Self employed'), ('Benefits', 'Benefits'),
                          ('Part time', 'Part time'), ('Temporary employment', 'Temporary employment'),
                          ('Student', 'Student'), ('Retired', 'Retired'), ('Contractor', 'Contractor'),
                          ('Zero hour contract', 'Zero hour contract'), ('Trainee','Trainee'))


class LoanApplication(models.Model):
    """Form to collect loan application data from customer"""
    loan_purpose = models.CharField(max_length=100, choices=purpose_list, default="")
    loan_amount = MoneyField(decimal_places=0, default_currency='GBP', max_digits=11,
                             validators=[MinValueValidator(1)])
    loan_term = models.CharField(max_length=100, choices=term_list)
    date_of_birth = models.DateField(max_length=10)
    marital_status = models.CharField(max_length=100, choices=marital_list, default="")
    children = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    residential_status = models.CharField(max_length=100, choices=residential_status_list, default="")
    residence_duration = models.IntegerField(default=0)
    employment_status = models.CharField(max_length=100, choices=employment_status_list, default="")
    monthly_salary = MoneyField(decimal_places=4, default=0, default_currency='GBP', max_digits=10,
                                validators=[MinValueValidator(1)])
    monthly_expenses = MoneyField(decimal_places=4, default=0, default_currency='GBP', max_digits=10,
                                  validators=[MinValueValidator(1)])
    monthly_rent = MoneyField(decimal_places=4, default=0, default_currency='GBP', max_digits=10,
                              validators=[MinValueValidator(1)])
    bankrupted = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.loan_amount})"


# project = models.FileField(upload_to='proiecte/', null=True, blank=True)
