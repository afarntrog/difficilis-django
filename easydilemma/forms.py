from django import forms
from django.forms import formset_factory


class DilemmaForm(forms.Form):
    dilemma_part_one = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Should I vote Democratic...'}))
    dilemma_part_two = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Or should I vote Republican...'}))



# TUTORIAL
class BookForm(forms.Form):
    name = forms.CharField(
        label='Book Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    )
BookFormset = formset_factory(BookForm, extra=1)