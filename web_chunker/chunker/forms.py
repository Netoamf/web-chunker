from django import forms
from .models import UserPreference, GrammarFile

ALGORITHM_CHOICES = [
    ('uchunker', 'UChunker'),
    # Adicione outros algoritmos aqui conforme necessário
]

class AlgorithmSelectionForm(forms.Form):
    algorithm = forms.ChoiceField(choices=ALGORITHM_CHOICES, label='Select Algorithm')

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=100, label='Grammar File Name')
    label = forms.CharField(max_length=100, label='Grammar File Label')
    file = forms.FileField()

class GrammarSelectionForm(forms.Form):
    grammar_files = forms.ModelMultipleChoiceField(
        queryset=GrammarFile.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Select Grammar Files'
    )
