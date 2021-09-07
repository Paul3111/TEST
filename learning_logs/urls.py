""" Defines  URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'  # this is the namespace (learning_logs) and index is a specific page in that namespace
urlpatterns = [
    #Home page.
    path('', views.index, name='index'),
    #Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    #Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    #Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    #Contact details page.
    path('contact/', views.contact, name='contact'),
    #Contact form.
    path('contact_form/', views.contact_form, name='contact_form'),
    #About us page.
    path('about_us/', views.about_us, name='about_us'),
    #Profile page.
    path('my_space/', views.my_space_view, name='my_space'),
    #Apply page.
    path('apply/', views.apply_loan, name='apply'),
    #Calculator page.
    path('calculator/', views.loan_calculator, name='calculator'),
    #Display loans page
    path('loans/', views.loans_display, name='loans'),
    #My loans page.
    path('my_loans/', views.my_loans, name='my_loans'),
    #Reports page.
    path('reports/', views.my_reports, name='reports'),
    #Quotes page.
    path('quotes/', views.my_quotes, name='quotes'),
    #Page to allow registered users to add their information
    path('customer_details/', views.customer_details, name='customer_details'),
]
