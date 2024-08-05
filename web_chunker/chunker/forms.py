# chunker/forms.py
from django import forms
from .models import UserPreference, Grammar

class GrammarForm(forms.ModelForm):
    class Meta:
        model = Grammar
        fields = ['sentence', 'gloss', 'translation']

class UserPreferenceForm(forms.ModelForm):
    class Meta:
        model = UserPreference
        fields = ['user', 'algorithm', 'other_preferences']
