from django.shortcuts import render, get_object_or_404
from .forms import DilemmaForm
from .models import DilemmaModel
# Create your views here.


def index(request):
    return render(request, 'easydilemma/index.html', context=None)


def dilemma(request):
    form = DilemmaForm()
    context = {
        "form": form
    }
    return render(request, 'easydilemma/dilemma.html', context)

# https://stackoverflow.com/a/936622 
# Problem this  is making a new dilemma each time. So you must make a new html template that does not create a new dilemma rather it just edits the field.
def edit_dilemma(request, dilemma_id):
    dilemma =  get_object_or_404(DilemmaModel, pk=dilemma_id)
    form = DilemmaForm(initial={'dilemma_part_one' : dilemma.dilemma_part_one, 'dilemma_part_two' : dilemma.dilemma_part_two})
    
    context = {
        "form": form
    }
    return render(request, 'easydilemma/dilemma.html', context)


def reasons(request):
    return render(request, 'easydilemma/reasons.html', context=None)


def all_dilemmas(request):
    return render(request, 'easydilemma/all_dilemmas.html', context=None)

def handle_dilemma(request):
    if request.method =='POST':
        form = DilemmaForm(request.POST)
        if form.is_valid():
            dilemma = DilemmaModel()
            dilemma.dilemma_part_one = form.cleaned_data['dilemma_part_one']
            dilemma.dilemma_part_two = form.cleaned_data['dilemma_part_two']
            dilemma.save()
            context = {
                "dilemma": dilemma
            }
            return render(request, 'easydilemma/reasons.html', context)
        else:
            pass

    form = DilemmaForm()
    return render(request, 'easydilemma/dilemma.html', {"form_1": form})

    # question = get_object_or_404(Question, pk=question_id)

    # try:
    #     dilemma_1 = request.POST['dilemma-part-1'])
    # except (KeyError, Choice.DoesNotExist):
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice"
    #     } )
    # else :
    #     selected_choice.votes += 1
    #     selected_choice.save()
        # return render(request, 'easydilemma/all_dilemmas.html', context=None)
