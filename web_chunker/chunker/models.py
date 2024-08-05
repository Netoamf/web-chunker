# chunker/models.py
from django.db import models

class GrammarFile(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class Grammar(models.Model):
    grammar_file = models.ForeignKey(GrammarFile, on_delete=models.CASCADE)
    sentence = models.TextField()
    gloss = models.TextField()
    translation = models.TextField()

class UserPreference(models.Model):
    user = models.CharField(max_length=100)
    algorithm = models.CharField(max_length=100)
    other_preferences = models.TextField(blank=True, null=True)

class AnalysisResult(models.Model):
    grammar = models.ForeignKey(Grammar, on_delete=models.CASCADE)
    result_data = models.TextField()
