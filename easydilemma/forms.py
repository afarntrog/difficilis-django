from django import forms

class DilemmaForm(forms.Form):
    dilemma_part_one = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Should I vote Democratic...'}))
    dilemma_part_two = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Or should I vote Republican...'}))