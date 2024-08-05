# chunker/models.py
from django.db import models

class Grammar(models.Model):
    sentence = models.TextField()
    gloss = models.TextField()
    translation = models.TextField()

class UserPreference(models.Model):
    algorithm_choices = [
        ('uchunker', 'UChunker'),
        # Outros algoritmos podem ser adicionados aqui
    ]
    user = models.CharField(max_length=100)
    algorithm = models.CharField(max_length=20, choices=algorithm_choices)
    other_preferences = models.JSONField()

class AnalysisResult(models.Model):
    grammar = models.ForeignKey(Grammar, on_delete=models.CASCADE)
    result_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
