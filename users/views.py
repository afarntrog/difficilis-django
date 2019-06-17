from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            # Redirect user to different page, use url name
            return redirect('easydilemma:index')
    else:
        # If not a POST request then return form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})