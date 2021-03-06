from django.shortcuts import render, get_object_or_404, redirect
from .forms import DilemmaForm
from .models import *
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import redirect, render
from django.core.paginator import Paginator # This is for pagination
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse


def index(request):
    return render(request, 'easydilemma/index.html', context=None)

def disclaimer(request):
    return render(request, 'easydilemma/disclaimer.html', context=None)

def dilemma(request):
    form = DilemmaForm()
    context = {
        "form": form
    }
    return render(request, 'easydilemma/dilemma.html', context)

# https://stackoverflow.com/a/936622 
# Problem this is making a new dilemma each time. So you must make a new html template that does not create a new dilemma rather it just edits the field.
def edit_dilemma(request, dilemma_id):
    dilemma =  get_object_or_404(Dilemma, pk=dilemma_id)
    # dilemma_part_1 = get_object_or_404(DilemmaPartOne, pk=dilemma_id)
    # dilemma_part_2 = get_object_or_404(DilemmaPartTwo, pk=dilemma_id)
    form = DilemmaForm(initial={'dilemma_part_one' : dilemma.dilemma_part_one, 'dilemma_part_two' : dilemma.dilemma_part_two})
    
    context = {
        "form": form,
        "dilemma": dilemma,
    }
    return render(request, 'easydilemma/edit_dilemma.html', context)





def reasons(request):
    return render(request, 'easydilemma/reasons.html', context=None)

def about_me(request):
    return render(request, 'easydilemma/aboutme.html', context=None)

# If the user clicks don't post in the dilemma_result page then it'll change the boolean field in model
def do_not_post(request, dilemma_id):
    my_dilemma = Dilemma.objects.get(id=dilemma_id)
    my_dilemma.should_post = False
    my_dilemma.save()
    return redirect('easydilemma:all_dilemmas')#all_dilemmas(request)#render(request, 'easydilemma/all_dilemmas.html', context=None)


def all_dilemmas(request):
    # Get this main dilemma pk
    get_all_dilemmas = Dilemma.objects.filter(should_post=True)

    # Only get all dilemmas that the boolea ield is set to true
    # [https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html]
    paginator = Paginator(get_all_dilemmas, 5)
    page = request.GET.get('page', 1)
    all_dilemmas = paginator.page(page)

    # Use the pks for each dilemma to get the current dilemma object to assccoiate with the reason
    context = {
        'all_dilemmas': all_dilemmas,
    }
    return render(request, 'easydilemma/all_dilemmas.html', context)


def popular_dilemmas(request):
    get_all_dilemmas = Dilemma.objects.filter(should_post=True).order_by('-vote_score')  

    # Only get all dilemmas that the boolea ield is set to true
    # [https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html]
    paginator = Paginator(get_all_dilemmas, 5)
    page = request.GET.get('page', 1)
    all_dilemmas = paginator.page(page)

    # Use the pks for each dilemma to get the current dilemma object to assccoiate with the reason
    context = {
        'all_dilemmas': all_dilemmas,
    }
    return render(request, 'easydilemma/all_dilemmas.html', context)



# This is for the newest dilemmas page
def newest_dilemmas(request):
    get_all_dilemmas = Dilemma.objects.filter(should_post=True).order_by('-created_date') # minus sign reverses the order.

    # Only get all dilemmas that the boolea ield is set to true
    # [https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html]
    paginator = Paginator(get_all_dilemmas, 5)
    page = request.GET.get('page', 1)
    all_dilemmas = paginator.page(page)

    # Use the pks for each dilemma to get the current dilemma object to assccoiate with the reason
    context = {
        'all_dilemmas': all_dilemmas,
    }
    return render(request, 'easydilemma/all_dilemmas.html', context)




# When a user clicks on another users name on a dilemma they can view all of the selected users
#   public dilemmas.
def username_public_dilemmas(request, username):
    # get_all_dilemmas that are for this user *and* `should_post=True`
    # `user__username` is the correct syntax when passing a primitive to the Django built in user model.
    get_all_dilemmas = Dilemma.objects.filter(user__username=username).filter(should_post=True)

    paginator = Paginator(get_all_dilemmas, 5)
    page = request.GET.get('page', 1)
    all_dilemmas = paginator.page(page)

    # Use the pks for each dilemma to get the current dilemma object to assccoiate with the reason
    context = {
        'all_dilemmas': all_dilemmas,
    }
    return render(request, 'easydilemma/all_dilemmas.html', context)





# Process the ajax like or dislike vote button.
@login_required
def handle_vote(request, dilemma_id):
    current_dilemma = Dilemma.objects.get(pk=dilemma_id)
    user = request.user # get the user who voted

    if request.is_ajax():
        status = request.GET.get('status')

        if status == 'vote_up':
            current_dilemma.votes.up(user.id)
        else:
            current_dilemma.votes.down(user.id)
        
        return JsonResponse(data={'score': current_dilemma.vote_score})

    
    # Not at all a json request
    return all_dilemmas(request)

    





# Return a user all of their dilemmas. Must be logged in.
@login_required
def all_user_dilemmas(request):
    # Get this main dilemma pk
    get_all_dilemmas = Dilemma.objects.filter(user=request.user)       

    # [https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html]
    paginator = Paginator(get_all_dilemmas, 5)
    page = request.GET.get('page', 1)
    all_dilemmas = paginator.page(page)

    # Use the pks for each dilemma to get the current dilemma object to assccoiate with the reason
    context = {
        'all_dilemmas': all_dilemmas,
    }
    return render(request, 'easydilemma/all_user_dilemmas.html', context)




def handle_dilemma(request):
    if request.method =='POST':
        form = DilemmaForm(request.POST)
        if form.is_valid():
            dilemma_1 = DilemmaPartOne()
            dilemma_2 = DilemmaPartTwo()
            dilemma_1.dilemma_part_one = form.cleaned_data['dilemma_part_one']
            dilemma_2.dilemma_part_two = form.cleaned_data['dilemma_part_two']
            dilemma_1.save()
            dilemma_2.save()


            dilemma = Dilemma()
            dilemma.dilemma_part_one = dilemma_1
            dilemma.dilemma_part_two = dilemma_2

            # If user is logged in then save it to dilemma model
            if request.user.is_authenticated:
                dilemma.user = request.user
            else:
                dilemma.user = None
            dilemma.save()

            context = {
                "dilemma": dilemma
            }
            return render(request, 'easydilemma/reasons.html', context)
        else:
            pass

    form = DilemmaForm()
    return render(request, 'easydilemma/dilemma.html', {"form_1": form})


def store_and_calc_reasons(request, dilemma_id):
    # Get this main dilemma pk
    my_dilemma = Dilemma.objects.get(id=dilemma_id)

    # data = request.POST.copy() When I have time i'll change this view to use this.

    # Get the pk for each dilemma side
    dilemma_1_id = my_dilemma.dilemma_part_one.id
    dilemma_2_id = my_dilemma.dilemma_part_two.id

    # Use the pks for each dilemma to get the current dilemma object to assccoiate with the reason
    dilemma_part_one = DilemmaPartOne.objects.get(id=dilemma_1_id)
    dilemma_part_two = DilemmaPartTwo.objects.get(id=dilemma_2_id)
    # Get the first form and all it's reasons and weights
    # print(request.POST.getlist('reason1'))
    
    all_reasons_1 = request.POST.getlist('reason1')
    all_select_elements_1 = request.POST.getlist('form-first-half-select')

    for i in range(len(all_reasons_1)):
        reason_model = ReasonPartOne()
        reason_model.reason = all_reasons_1[i]

        reason_model.selected_option = all_select_elements_1[i]
        reason_model.dilemma = dilemma_part_one
        reason_model.save()

    # Get the second form and all it's reasons and weights.
    all_reason_2 = request.POST.getlist('reason_2')
    all_select_elements_2 = request.POST.getlist('form-second-half-select')

    for i in range(len(all_reason_2)):
        reason_model = ReasonPartTwo()
        reason_model.reason = all_reason_2[i]

        reason_model.selected_option = all_select_elements_2[i]
        reason_model.dilemma = dilemma_part_two
        reason_model.save()

    # Get the winning dilemma side.
    dilemma_result = calculate_result(request, all_select_elements_1, all_select_elements_2,my_dilemma )
    # Save winning dilemma side to the currnt Dilemm model result field
    my_dilemma.result = dilemma_result
    my_dilemma.save()


    # # Get a list of all the reason objects for each side of the dilemma 
    list_of_reasons_one = ReasonPartOne.objects.filter(dilemma=dilemma_part_one)
    list_of_reasons_two = ReasonPartTwo.objects.filter(dilemma=dilemma_part_two)

    # Store model data for use in the template
    context = {
        'dilemma': my_dilemma,
        'full_dilemma': f"Should I {my_dilemma.dilemma_part_one} Or should I {my_dilemma.dilemma_part_two}",
        'dilemma_part_one': my_dilemma.dilemma_part_one,
        'dilemma_part_two': my_dilemma.dilemma_part_two,
        'all_dilemma_one_reasons': list_of_reasons_one,
        'all_dilemma_two_reasons': list_of_reasons_two,
        'result': dilemma_result,
    }

    return render(request, 'easydilemma/dilemma_result.html', context)

 

# This will simply calculate and return the result which side is better
def calculate_result(request, all_select_elements_1, all_select_elements_2, my_dilemma ):
    total_dilemma_1 = 0
    for val in all_select_elements_1:
        total_dilemma_1 += int(val)
    
    total_dilemma_2 = 0
    for val in all_select_elements_2:
        total_dilemma_2 += int(val)
    
    if total_dilemma_1 > total_dilemma_2:
        return my_dilemma.dilemma_part_one.dilemma_part_one
    else:
        return my_dilemma.dilemma_part_two.dilemma_part_two
    

def handle_revised_dilemma(request, dilemma_id):
    if request.method =='POST':
        form = DilemmaForm(request.POST)

        if form.is_valid():
            dilemma_1 = DilemmaPartOne()
            dilemma_2 = DilemmaPartTwo()
            dilemma_1.dilemma_part_one = form.cleaned_data['dilemma_part_one']
            dilemma_2.dilemma_part_two = form.cleaned_data['dilemma_part_two']
            dilemma_1.save()
            dilemma_2.save()

            # We are revising a dilemma, so get the Dilemma that we need to update
            dilemma = Dilemma(id=dilemma_id)
            dilemma.dilemma_part_one = dilemma_1
            dilemma.dilemma_part_two = dilemma_2
            dilemma.save()

            context = {
                "dilemma": dilemma
            }
            return render(request, 'easydilemma/reasons.html', context)
        else:
            # Add message here, popup alert or something
            pass


    # If for some reason the revised form is not valid then redisplay the form with the prefilled 
    # ... data that they wanted to revise
    dilemma =  get_object_or_404(Dilemma, pk=dilemma_id)
    dilemma_part_1 = get_object_or_404(DilemmaPartOne, pk=dilemma_id)
    dilemma_part_2 = get_object_or_404(DilemmaPartTwo, pk=dilemma_id)
    form = DilemmaForm(initial={'dilemma_part_one' : dilemma.dilemma_part_one, 'dilemma_part_two' : dilemma.dilemma_part_two})
    
    return render(request, 'easydilemma/dilemma.html', {"form_1": form})








# Search dilemmas
# Search results for job posts
def search_results(request):
    query = request.GET.get('q')

    if query:
        all_dilemmas = Dilemma.objects.filter(dilemma_part_one__dilemma_part_one__icontains=query, should_post=True) | Dilemma.objects.filter(dilemma_part_two__dilemma_part_two__icontains=query, should_post=True)
    try:
        # Pagination
        paginator = Paginator(all_dilemmas, 5)
        page = request.GET.get('page', 1)
        all_dilemmas = paginator.page(page)
    except:
            pass
            
    context = {
        'all_dilemmas': all_dilemmas,
        'query': query, # Needed for pagiantion, avoid 'local variable 'all_dilemmas' referenced before assignment'
    }

    return render(request, 'easydilemma/all_dilemmas.html', context)