from django.db import models
from django.contrib.auth.models import User
# import phonenumber_field


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
    contact_number = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50, blank=True)
    address_line3 = models.CharField(max_length=50, blank=True)
    address_city = models.CharField(max_length=50)
    address_county = models.CharField(max_length=50)
    address_post_code = models.CharField(max_length=50)
    address_country = models.CharField(max_length=50)
    # user_id = UserInformation.objects.filter()
    alerts = models.BooleanField(default=False)
    newsletter_selection = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "InfoUsers"

    def __str__(self):
        """To display these fields in the admin panel"""
        return f"{self.first_name} {self.last_name} - {self.email}. Added on: {self.date_created}"
