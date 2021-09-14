from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


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
    profile_picture = models.ImageField(upload_to='photos', blank=True, null=True)
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
        return f"Date: {self.date_added}. Subject: {self.customer_message_subject[:50]}." \
               f" Message: {self.customer_message[:50]}[...]."
