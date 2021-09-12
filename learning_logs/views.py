from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry, UserInformation
from .forms import TopicForm, EntryForm, UserInformationForm


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Show all topics"""
    # topics = Topic.objects.order_by('date_added')
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    #Make sure the topic belongs to the current user
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        #No data submitted; create a blank form.
        form = TopicForm()
    else:
        #POST data submitted, process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    #Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No Data submitted, create a blank form.
        form = EntryForm()
    else:
        # POST data submitted, process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        """Initial request, pre-fill form with the current entry."""
        form = EntryForm(instance=entry)
    else:
        """POST data submitted; process data."""
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def contact(request):
    """The contact page."""
    return render(request, 'learning_logs/contact.html')


@login_required()
def contact_form(request):
    """The contact form."""
    return render(request, 'learning_logs/contact_form.html')


def about_us(request):
    """The About us page."""
    return render(request, 'learning_logs/about_us.html')


@login_required()
def my_space_view(request, auth_user_id):
    """The profile page"""
    # user_personal_data = UserInformation.objects.filter(owner=auth_user_id)
    user_personal_data = UserInformation.objects.get(owner=auth_user_id)
    if UserInformation.objects.get(id=auth_user_id).owner != request.user:
        raise Http404
    context = {'user_personal_data': user_personal_data}
    return render(request, 'learning_logs/my_space.html', context)


# def test(request):
#     img = Photo.objects.all().order_by('-id')
#     return render_to_response("my_space.html", {"img": img})


@login_required()
def apply_loan(request):
    """The page where you can apply for a loan"""
    return render(request, 'learning_logs/apply.html')


def loan_calculator(request):
    """This page displays the loan calculator"""
    return render(request, 'learning_logs/calculator.html')


def loans_display(request):
    """This page displays all the loans"""
    return render(request, 'learning_logs/loans.html')


@login_required()
#to use user's id?
def my_loans(request):
    """This page displays a user's loans and additional information"""
    return render(request, 'learning_logs/my_loans.html')


@login_required()
#to use user's id
def my_reports(request):
    """To allow the user to display reports and to view charts"""
    return render(request, 'learning_logs/reports.html')


@login_required()
#to use user's id
def my_quotes(request):
    """To display saved quotes"""
    return render(request, 'learning_logs/quotes.html')


@login_required()
def customer_details(request):
    """To allow users to enter and amend their personal data. When done, to redirect to my_space"""

    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = UserInformationForm()
    else:
        #POST data submitted; process data.
        form = UserInformationForm(data=request.POST)
        if form.is_valid():
            customer_details = form.save(commit=False)  # trying to link the data with the logged in user
            customer_details.owner = request.user   # trying to link the data with the logged in user
            customer_details.save()     # trying to link the data with the logged in user
            # form.save()   # you only need to save the form, if data no linked to user
            return redirect('learning_logs:my_space/')

    #Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/customer_details.html', context)

