from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
# Create your views here.

# Imported for letting user know he logged out.
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib import messages
# This will log the user in automatically after signup!
from django.contrib.auth import authenticate, login

# For delete view
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# For delete specific dilemma
from easydilemma.models import Dilemma
from django.core.exceptions import ObjectDoesNotExist


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! You have successfully created an account👏')

            # This will log the user in automatically after signup!
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            
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



# Delete user account
@login_required
def del_user(request):    
    try:
        u = User.objects.get(username = request.user)
        u.delete()
        messages.success(request, "You successfully deleted your account.")            

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")    
        return redirect('easydilemma:index') 

    return redirect('easydilemma:index') 



# Delete user account
@login_required
def del_dilemma(request, dilemma_id):    
    try:
        Dilemma.objects.filter(id=dilemma_id).delete()
        messages.success(request, "Dilemma successfully deleted.")            

    except dilemma_id.DoesNotExist:
        messages.error(request, "Dilemma does not exist")    
        return redirect('easydilemma:all_user_dilemmas') 

    return redirect('easydilemma:all_user_dilemmas') 



# Delete user account
@login_required
def make_public(request, dilemma_id):    
    try:
        dilemma = Dilemma.objects.get(id=dilemma_id)
        dilemma.should_post = True
        dilemma.save()
        messages.success(request, "Dilemma successfully posted.")            

    except ObjectDoesNotExist:
        messages.error(request, "Dilemma does not exist")    
        return redirect('easydilemma:all_user_dilemmas')

    return redirect('easydilemma:all_user_dilemmas') 


# Delete user account
@login_required
def make_private(request, dilemma_id):    
    try:
        dilemma = Dilemma.objects.get(id=dilemma_id)
        dilemma.should_post = False
        dilemma.save()
        messages.success(request, "Dilemma is now private.")            

    except ObjectDoesNotExist:
        messages.error(request, "Dilemma does not exist")    
        return redirect('easydilemma:all_user_dilemmas')

    return redirect('easydilemma:all_user_dilemmas') 




@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('easydilemma:index')

    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form
        }

    return render(request, 'users/profile_update.html', context)