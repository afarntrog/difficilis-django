from django import forms
from django.forms import formset_factory
# from django.forms.formsets import BaseFormSet

class DilemmaForm(forms.Form):
    dilemma_part_one = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Should I vote Democratic...'}))
    dilemma_part_two = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Or should I vote Republican...'}))
