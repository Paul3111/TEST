import os
import random
import csv
from matplotlib import pyplot as plt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from .models import Topic, Entry, UserInformation, CustomerMessage, LoanApplication, LoanCalculation
from .forms import TopicForm, EntryForm, UserInformationForm, CustomerMessageForm, LoanApplicationForm,\
    LoanCalculationForm
import mimetypes
import requests
import matplotlib
matplotlib.use('Agg')


def index(request):
    """The home page for Learning Log."""
    response = requests.get('http://data.fixer.io/api/latest?access_key=73ea8da135eb2dd7f6150c05cd8c75ec')
    json_response = response.json()
    result = json_response['rates']
    fx_date = json_response['date']
    return render(request, 'learning_logs/index.html', {'result': result, 'date': fx_date})


@login_required
def topics(request):
    """Show all topics"""
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
def contact_form(request, auth_user_id):
    """To send messages"""
    if auth_user_id != request.user.id:
        raise Http404

    if request.method == 'POST':
        form = CustomerMessageForm(data=request.POST)
        if form.is_valid():
            contact_form = form.save(commit=False)
            contact_form.owner = request.user
            contact_form.save()
            return redirect(f'/contact/')
        context = {'form': form}
        return render(request, 'learning_logs/contact_form.html', context)
    return render(request, 'learning_logs/contact_form.html', {'form': CustomerMessageForm()})


def about_us(request):
    """The About us page."""
    return render(request, 'learning_logs/about_us.html')


@login_required()
def my_space_view(request, auth_user_id):
    """The profile page"""
    user_personal_data = UserInformation.objects.get(owner=auth_user_id)
    if UserInformation.objects.get(id=auth_user_id).owner != request.user:
        raise Http404

    context = {'user_personal_data': user_personal_data}
    return render(request, 'learning_logs/my_space.html', context)


def download_application_form(request):
    """Used to allow the user to download forms on the APPLY page"""
    la_file_path = 'media/'
    filename = 'ApplicationForm.pdf'

    file = open(os.path.join(os.path.dirname('media'), 'ApplicationForm.pdf'), 'r')
    mime_type, _ = mimetypes.guess_type(la_file_path)
    response = HttpResponse(file, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return render(request, 'learning_logs/apply.html')


@login_required
def apply_loan(request, auth_user_id):
    """Used to enter data and apply online"""
    if auth_user_id != request.user.id:
        raise Http404

    def monthly_loan(principal2, interest_rate2, duration2):
        """Calculates the monthly repayment"""
        n = int(duration2) * 12
        r = float(interest_rate2) / (100 * 12)
        monthly_payment2 = int(principal2) * ((r * ((r + 1) ** n)) / (((r + 1) ** n) - 1))
        return monthly_payment2

    def remaining_balance(principal2, interest_rate2, duration2, payments2):
        """Calculates the remaining BALANCE after x payments made"""
        r = interest_rate2 / 1200
        m = r + 1
        n = duration2 * 12
        remaining2 = int(principal2) * (((m ** n) - (m ** int(payments2))) / ((m ** n) - 1))
        return remaining2

    def total_cost(pr, m_rate, pmts):
        """Calculates the total interest"""
        r = m_rate / 1200
        n = pmts * 12
        loan_total2 = (int(pr) * float(r) * int(n)) / (1 - ((1+float(r))**int(-n)))
        return loan_total2

    if request.method == 'POST':
        form = LoanApplicationForm(request.POST, request.FILES)

        loan_amount = form.data['loan_amount']
        interest_rate = form.data['interest_rate']
        loan_term = form.data['loan_term']

        repayment = round(monthly_loan(int(loan_amount), float(interest_rate), int(loan_term)), 2)
        fees = round(total_cost(int(loan_amount), float(interest_rate), int(loan_term)) - int(loan_amount), 2)
        loan_total = round(remaining_balance(int(loan_amount), float(interest_rate), int(loan_term), 0) + fees, 2)
        take_home = int(loan_total - fees)

        if form.is_valid():

            apply_loan = form.save(commit=False)
            apply_loan.owner = request.user
            apply_loan.monthly_payment = repayment
            apply_loan.fees = fees
            apply_loan.loan_total = loan_total
            apply_loan.take_home = take_home
            apply_loan.save()

            def PMT(rate, nper, pv, fv=0, type=0):
                if rate != 0:
                    pmt = (float(rate) * (fv + pv * (1 + float(rate)) ** nper)) / ((1 + float(rate) * type) * (1 - (1 + float(rate)) ** nper))
                else:
                    pmt = (-1 * (fv + pv) / nper)
                return (pmt)

            def IPMT(rate, per, nper, pv, fv=0, type=0):
                ipmt = -(((1 + float(rate)) ** (per - 1)) * (pv * float(rate) + PMT(float(rate), nper, pv, fv=0, type=0)) - PMT(float(rate), nper,pv, fv=0, type=0))
                return (ipmt)

            def PPMT(rate, per, nper, pv, fv=0, type=0):
                ppmt = PMT(float(rate), nper, pv, fv=0, type=0) - IPMT(float(rate), per, nper, pv, fv=0, type=0)
                return (ppmt)

            interest_rate_rs = float(interest_rate) / 100
            remaining_balance = float(loan_amount)
            rs_file = open(f'media/rs{auth_user_id}_{apply_loan.id}.csv', 'w', newline="")
            writer = csv.writer(rs_file)
            writer.writerow(['Instalment no.', 'Monthly payment', 'Principal', 'Interest', 'Balance'])

            for i in range(1, (int(loan_term) * 12) + 1):
                monthly_instalment = PMT(float(interest_rate_rs) / 12, 12 * int(loan_term), float(loan_amount))
                principal = PPMT(float(interest_rate_rs) / 12, i, 12 * int(loan_term), float(loan_amount))
                interest_rs = IPMT(float(interest_rate_rs) / 12, i, 12 * int(loan_term), float(loan_amount))
                line = f'Instalment {i}', -round(float(monthly_instalment), 2), -round(float(principal), 2),\
                       -round(float(interest_rs), 2), round(remaining_balance + float(principal), 2)
                remaining_balance += float(principal)
                writer.writerow(line)

            rs_file.close()

            return redirect(f'/my_space/{auth_user_id}/')

        context = {'form': form, 'repayment': repayment, 'loan_total': loan_total, 'fees': fees,
                   'take_home': take_home}
        return render(request, 'learning_logs/apply_online.html', context)

    else:
        return render(request, 'learning_logs/apply_online.html', {'form': LoanApplicationForm()})


@login_required()
def view_loan_request(request, loan_id):
    """To view each loan request"""
    individual_loan_req = LoanApplication.objects.get(id=loan_id)

    if individual_loan_req.owner != request.user:
        raise Http404

    fee_data = individual_loan_req.fees
    take_home_data = individual_loan_req.take_home

    labels = 'Fees', 'Take Home'
    sizes = [fee_data, take_home_data]
    explode = (0.1, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.savefig('media/loan_chart.png', dpi=100)

    context = {'individual_loan_req': individual_loan_req}
    return render(request, 'learning_logs/view_loan_request.html', context)


@login_required()
def loan_calculator(request, auth_user_id):
    """This page displays the loan calculator and saves the calculations"""

    if auth_user_id != request.user.id:
        raise Http404

    def monthly_loan(principal, interest_rate, duration):
        """Calculates the monthly repayment"""
        n = int(duration) * 12
        r = float(interest_rate) / (100 * 12)
        monthly_payment = int(principal) * ((r * ((r + 1) ** n)) / (((r + 1) ** n) - 1))
        return monthly_payment

    def remaining_balance(principal, interest_rate, duration, payments):
        """Calculates the remaining BALANCE after x payments made"""
        r = interest_rate / 1200
        m = r + 1
        n = duration * 12
        remaining = int(principal) * (((m ** n) - (m ** int(payments))) / ((m ** n) - 1))
        return remaining

    # print('this is remaining after X payments 100.000 , 8% , 10 years, 119 pmts', remaining_balance(100000, 8, 10, 119))

    def total_cost(pr, m_rate, pmts):
        """Calculates the total interest"""
        r = m_rate / 1200
        n = pmts * 12
        loan_total = (int(pr) * float(r) * int(n)) / (1 - ((1+float(r))**int(-n)))
        return loan_total

    if request.method == 'POST':
        form = LoanCalculationForm(data=request.POST)
        if form.is_valid():
            principal = form.data['principal']
            interest_rate = form.data['interest_rate']
            duration = form.data['duration']

            repayment = round(monthly_loan(int(principal), float(interest_rate), int(duration)), 2)
            fees = round(total_cost(int(principal), float(interest_rate), int(duration)) - int(principal), 2)
            loan_total = round(remaining_balance(int(principal), float(interest_rate), int(duration), 0) + fees, 2)
            take_home = int(loan_total - fees)

            loan_calculator = form.save(commit=False)
            loan_calculator.owner = request.user
            loan_calculator.monthly_payment = repayment
            loan_calculator.save()

            context = {'form': form, 'repayment': repayment, 'loan_total': loan_total, 'fees': fees,
                       'take_home': take_home}
            return render(request, 'learning_logs/calculator.html', context)

    else:
        form = LoanCalculationForm(data=request.POST)
        context = {'form': form}
        return render(request, 'learning_logs/calculator.html', context)


def loans_display(request):
    """This page displays all the loans that the company can sell, not the user's loans list!"""
    return render(request, 'learning_logs/loans.html')


@login_required()
def my_loans(request, auth_user_id):
    """This page displays a user's loans and additional information"""
    user_loans = LoanApplication.objects.filter(owner=auth_user_id)

    if auth_user_id != request.user.id:
        raise Http404

    context = {'user_loans': user_loans}
    return render(request, 'learning_logs/my_loans.html', context)


@login_required()
def my_reports(request):
    """To allow the user to display reports and to view charts"""
    labels = 'Sale', 'Purchase'
    sizes = [random.randint(10, 30), random.randint(30, 50)]
    explode = (0.1, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.savefig('media/loan_chart.png', dpi=100)
    return render(request, 'learning_logs/reports.html')


@login_required()
def my_messages(request, auth_user_id):
    """To display saved messages"""
    user_messages = CustomerMessage.objects.filter(owner=auth_user_id)

    if auth_user_id != request.user.id:
        raise Http404

    context = {'user_messages': user_messages}
    return render(request, 'learning_logs/messages.html', context)


@login_required()
def customer_details(request, auth_user_id):
    """To allow users to enter and amend their personal data. When done, to redirect to my_space"""
    existing_data = UserInformation.objects.get(owner=auth_user_id)

    if UserInformation.objects.get(id=auth_user_id).owner != request.user:
        raise Http404

    if request.method != 'POST':
        #No data submitted; create a blank form and fetch existing data.
        form = UserInformationForm(instance=existing_data)
    else:
        #POST data submitted; process data.
        form = UserInformationForm(request.POST, request.FILES, instance=existing_data)
        if form.is_valid():
            customer_details = form.save(commit=False)
            customer_details.owner = request.user
            customer_details.save()
            return redirect(f'/my_space/{customer_details.id}/')

    #Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/customer_details.html', context)


@login_required()
def read_message(request, message_id):
    """Show each message"""
    message = CustomerMessage.objects.get(id=message_id)

    if message.owner != request.user:
        raise Http404

    context = {'message': message}
    return render(request, 'learning_logs/read_message.html', context)
