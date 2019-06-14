from django.shortcuts import render, get_object_or_404, redirect
from .forms import DilemmaForm
from .models import *
# Create your views here.
from django.http import HttpResponse


# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse
# from django.db import IntegrityError, transaction
# from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render




def index(request):
    return render(request, 'easydilemma/index.html', context=None)


def dilemma(request):
    form = DilemmaForm()
    context = {
        "form": form
    }
    return render(request, 'easydilemma/dilemma.html', context)

# https://stackoverflow.com/a/936622 
# Problem this is making a new dilemma each time. So you must make a new html template that does not create a new dilemma rather it just edits the field.
def edit_dilemma(request, dilemma_id):
    dilemma =  get_object_or_404(DilemmaModel, pk=dilemma_id)
    dilemma_part_1 = get_object_or_404(DilemmaPartOne, pk=dilemma_id)
    dilemma_part_2 = get_object_or_404
    form = DilemmaForm(initial={'dilemma_part_one' : dilemma.dilemma_part_one, 'dilemma_part_two' : dilemma.dilemma_part_two})
    
    context = {
        "form": form
    }
    return render(request, 'easydilemma/dilemma.html', context)


def reasons(request):
    return render(request, 'easydilemma/reasons.html', context=None)


def all_dilemmas(request):
    # Get this main dilemma pk
    all_dilemmas = Dilemma.objects.all()

    # Get the pk for each dilemma side
    # dilemma_1 = my_dilemma.dilemma_part_one
    # dilemma_2 = my_dilemma.dilemma_part_two
    # # print(dilemma_1_id.reason_part_one.all)
    # for item in dilemma_1.reason_part_one.all():
    #     print(item)

    for dilemma in all_dilemmas:
        dilemma_first_half = dilemma.dilemma_part_one
        dilemma_second_half = dilemma.dilemma_part_two

        for reason in dilemma_first_half.reason_part_one.all():
            print(reason.reason)
            print(reason.selected_option)

    #### USE ^^^^^ THis method for looping throught the dilemma object in th template
    # Use the pks for each dilemma to get the current dilemma object to assccoiate with the reason
    # dilemma_part_one = DilemmaPartOne.objects.get(id=dilemma_1_id)
    context = {
        'dilemma': all_dilemmas,
    }

    return render(request, 'easydilemma/all_dilemmas.html', context)

# def handle_dilemma(request):
#     if request.method =='POST':
#         form = DilemmaForm(request.POST)
#         if form.is_valid():
#             dilemma = DilemmaModel()
#             dilemma.dilemma_part_one = form.cleaned_data['dilemma_part_one']
#             dilemma.dilemma_part_two = form.cleaned_data['dilemma_part_two']
#             dilemma.save()
#             context = {
#                 "dilemma": dilemma
#             }
#             return render(request, 'easydilemma/reasons.html', context)
#         else:
#             pass

#     form = DilemmaForm()
#     return render(request, 'easydilemma/dilemma.html', {"form_1": form})


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
            dilemma.save()

            context = {
                "dilemma": dilemma
            }
            return render(request, 'easydilemma/reasons.html', context)
        else:
            pass

    form = DilemmaForm()
    return render(request, 'easydilemma/dilemma.html', {"form_1": form})


def test_reason(request, dilemma_id):

    # Get this main dilemma pk
    my_dilemma = Dilemma.objects.get(id=dilemma_id)

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
    dilemma_result = result(request, all_select_elements_1, all_select_elements_2,my_dilemma )


    # Get a list of all the reason objects for each side of the dilemma 
    list_of_reasons_one = ReasonPartOne.objects.filter(dilemma=dilemma_part_one)
    list_of_reasons_two = ReasonPartTwo.objects.filter(dilemma=dilemma_part_two)

    # Store model data for use in the template
    context = {
        'full_dilemma': f"Should I {my_dilemma.dilemma_part_one} Or should I {my_dilemma.dilemma_part_two}",
        'dilemma_part_one': my_dilemma.dilemma_part_one,
        'dilemma_part_two': my_dilemma.dilemma_part_two,
        'all_dilemma_one_reasons': list_of_reasons_one,
        'all_dilemma_two_reasons': list_of_reasons_two,
        'result': dilemma_result,
    }

    return render(request, 'easydilemma/dilemma_result.html', context)
 

# This will simply calculate and return the result which side is better
def result(request, all_select_elements_1, all_select_elements_2, my_dilemma ):
    total_dilemma_1 = 0
    for val in all_select_elements_1:
        total_dilemma_1 += int(val)
    
    total_dilemma_2 = 0
    for val in all_select_elements_2:
        total_dilemma_2 += int(val)
    
    if total_dilemma_1 > total_dilemma_2:
        return my_dilemma.dilemma_part_one
    else:
        return my_dilemma.dilemma_part_two
    
