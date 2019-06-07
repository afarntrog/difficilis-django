from django.shortcuts import render, get_object_or_404, redirect
from .forms import DilemmaForm, BookFormset
from .models import DilemmaModel, Book
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

 





def create_book_normal(request):
    template_name = 'easydilemma/create_normal.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = BookFormset(request.GET or None)
    elif request.method == 'POST':
        formset = BookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    Book(name=name).save()
            # once all books are saved, redirect to book list view
            return redirect('book_list')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })