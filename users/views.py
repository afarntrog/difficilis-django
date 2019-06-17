from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

# Imported for letting user know he logged out.
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome👏 Account created for {username}!')

            # Redirect user to different page, use url name
            return redirect('easydilemma:index')
    else:
        # If not a POST request then return form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



# This will display a message to the user letting him know he logged out.
# https://stackoverflow.com/a/19379676/11576212
@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, 'You have successfully logged out.')