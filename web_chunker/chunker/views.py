# chunker/views.py
from django.shortcuts import render, redirect
from .models import Grammar, UserPreference, AnalysisResult
from .forms import GrammarForm, UserPreferenceForm
from .uchunker import run_uchunker

def load_grammar(request):
    if request.method == 'POST':
        form = GrammarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('load_grammar')
    else:
        form = GrammarForm()
    return render(request, 'chunker/load_grammar.html', {'form': form})

def set_preferences(request):
    if request.method == 'POST':
        form = UserPreferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('set_preferences')
    else:
        form = UserPreferenceForm()
    return render(request, 'chunker/set_preferences.html', {'form': form})

def run_analysis(request):
    preferences = UserPreference.objects.last()
    grammars = Grammar.objects.all()
    results = []

    if preferences.algorithm == 'uchunker':
        for grammar in grammars:
            result = run_uchunker(grammar)
            analysis_result = AnalysisResult(grammar=grammar, result_data=result)
            analysis_result.save()
            results.append(analysis_result)

    return render(request, 'chunker/results.html', {'results': results})

def index(request):
    return render(request, 'chunker/index.html')
