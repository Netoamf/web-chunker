# chunker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('load-grammar/', views.load_grammar, name='load_grammar'),
    path('set-preferences/', views.set_preferences, name='set_preferences'),
    path('run-analysis/', views.run_analysis, name='run_analysis'),
]
