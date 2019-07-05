from django import forms
from django.forms import formset_factory
# from django.forms.formsets import BaseFormSet

class DilemmaForm(forms.Form):
    dilemma_part_one = forms.CharField(label='Should I', widget=forms.TextInput(attrs={'placeholder': 'Vote Democratic...'}))
    dilemma_part_two = forms.CharField(label='Or should I',widget=forms.TextInput(attrs={'placeholder': 'Vote Republican...'}))
