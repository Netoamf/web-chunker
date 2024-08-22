from django.contrib import admin
from .models import GrammarFile, Grammar, UserPreference, AnalysisResult

@admin.register(GrammarFile)
class GrammarFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'label')

@admin.register(Grammar)
class GrammarAdmin(admin.ModelAdmin):
    list_display = ('grammar_file', 'sentence', 'gloss', 'translation')

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'algorithm', 'other_preferences')

@admin.register(AnalysisResult)
class AnalysisResultAdmin(admin.ModelAdmin):
    list_display = ('grammar', 'result_data')
