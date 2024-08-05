# chunker/admin.py
from django.contrib import admin
from .models import Grammar, UserPreference, AnalysisResult

admin.site.register(Grammar)
admin.site.register(UserPreference)
admin.site.register(AnalysisResult)
