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
    path('contact_form/<int:auth_user_id>/', views.contact_form, name='contact_form'),
    #About us page.
    path('about_us/', views.about_us, name='about_us'),
    #Profile page.
    path('my_space/<int:auth_user_id>/', views.my_space_view, name='my_space'),
    #Apply page.
    path('apply/', views.download_application_form, name='apply'),
    #Apply online page
    path('apply_online/<int:auth_user_id>/', views.apply_loan, name='apply_online'),
    #Calculator page.
    path('calculator/<int:auth_user_id>/', views.loan_calculator, name='calculator'),
    #Display loans page, the page where you see all the types of loans
    path('loans/', views.loans_display, name='loans'),
    #My loans page.
    path('my_loans/<int:auth_user_id>/', views.my_loans, name='my_loans'),
    #To view a single loan and all the data
    path('view_loan_request/<int:loan_id>/', views.view_loan_request, name='view_loan_request'),
    #Reports page.
    path('reports/', views.my_reports, name='reports'),
    #Messages page.
    path('messages/<int:auth_user_id>/', views.my_messages, name='messages'),
    #Page to allow registered users to add their information
    path('customer_details/<int:auth_user_id>/', views.customer_details, name='customer_details'),
    #Page that displays an individual message so the user can read it
    path('read_message/<int:message_id>/', views.read_message, name='read_message'),
]
