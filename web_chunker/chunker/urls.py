from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload_file'),
    path('select-algorithm/', views.select_algorithm, name='select_algorithm'),
    path('select-grammar/', views.select_grammar, name='select_grammar'),
    path('run-selected-analysis/<str:grammar_file_ids>/', views.run_selected_analysis, name='run_selected_analysis'),
]
