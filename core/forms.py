from django import forms
from .models import Responder
import tagulous.models


class InputForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    AGE_CHOICES = (
        (1, 'Below 16 years old'),
        (2, 'From 16 - 32 years old'),
        (3, 'From 32 - 45 years old'),
        (4, 'From 45 - 60 years old'),
        (5, 'From 60 - 81 years old'),
        (6, 'Above 81 years old')
    )
    RELATION_CHOICES = (
        (1, 'Family'),
        (2, 'Friend'),
        (3, 'Co-worker'),
        (4, 'Acquintance'),
        (5, 'Other'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    age = forms.ChoiceField(choices=AGE_CHOICES, widget=forms.RadioSelect())
    relation = forms.ChoiceField(choices=RELATION_CHOICES, widget=forms.RadioSelect())

    class Meta:
        fields = ['code', 'gender', 'age', 'relation', 'words']
        labels = {'words': '10 adjectives for her/him:'}
        model = Responder
