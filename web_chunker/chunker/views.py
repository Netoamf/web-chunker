from django.shortcuts import render, redirect, get_object_or_404
from .models import Grammar, UserPreference, AnalysisResult, GrammarFile
from .forms import AlgorithmSelectionForm, UploadFileForm, GrammarSelectionForm
from .uchunker import run_uchunker
import os

def index(request):
    return render(request, 'chunker/index.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            label = form.cleaned_data['label']
            handle_uploaded_file(request.FILES['file'], name, label)
            return redirect('index')
    else:
        form = UploadFileForm()
    return render(request, 'chunker/upload.html', {'form': form})

def handle_uploaded_file(f, name, label):
    upload_dir = os.path.join(os.path.dirname(__file__), 'uploads')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file_path = os.path.join(upload_dir, f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    process_uploaded_file(file_path, name, label)

def process_uploaded_file(file_path, name, label):
    grammar_file = GrammarFile.objects.create(name=name, label=label)
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            sentence = lines[i].strip()
            gloss = lines[i+1].strip()
            translation = lines[i+2].strip()
            Grammar.objects.create(grammar_file=grammar_file, sentence=sentence, gloss=gloss, translation=translation)

def select_algorithm(request):
    if request.method == 'POST':
        form = AlgorithmSelectionForm(request.POST)
        if form.is_valid():
            user_preference, created = UserPreference.objects.get_or_create(user='default_user')
            user_preference.algorithm = form.cleaned_data['algorithm']
            user_preference.save()
            return redirect('select_grammar')
    else:
        form = AlgorithmSelectionForm()
    return render(request, 'chunker/select_algorithm.html', {'form': form})

def select_grammar(request):
    if request.method == 'POST':
        form = GrammarSelectionForm(request.POST)
        if form.is_valid():
            selected_grammar_files = form.cleaned_data['grammar_files']
            grammar_file_ids = [file.id for file in selected_grammar_files]
            return redirect('run_selected_analysis', grammar_file_ids=','.join(map(str, grammar_file_ids)))
    else:
        form = GrammarSelectionForm()
    return render(request, 'chunker/select_grammar.html', {'form': form})

def run_selected_analysis(request, grammar_file_ids):
    grammar_file_ids = grammar_file_ids.split(',')
    grammars = Grammar.objects.filter(grammar_file__id__in=grammar_file_ids)
    preferences = UserPreference.objects.last()

    if not preferences:
        return render(request, 'chunker/results.html', {'results': [], 'error': 'User preferences not set.'})

    results = []
    if preferences.algorithm == 'uchunker':
        for grammar in grammars:
            result = run_uchunker(grammar)
            analysis_result = AnalysisResult(grammar=grammar, result_data=result)
            analysis_result.save()
            results.append(analysis_result)

    return render(request, 'chunker/results.html', {'results': results})
