from django.contrib import admin
from .models import Topic, Entry, UserInformation, CustomerMessage, LoanApplication, LoanCalculation

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(UserInformation)
admin.site.register(CustomerMessage)
admin.site.register(LoanApplication)
admin.site.register(LoanCalculation)
