from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from learning_logs.models import UserInformation


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        #Display blank registration form
        form = UserCreationForm
    else:
        #Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            UserInformation.objects.update_or_create(id=new_user.id, owner_id=new_user.id)
            #Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect(f'/customer_details/{new_user.id}/')

    #Display a blank of invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
