# pythongames/urls.py
from django.urls import path
from . import views

app_name = 'pythongames'

urlpatterns = [
    path('hangman/', views.hangman, name='hangman'),
    path('restart/', views.restart_game, name='restart'),
    path('quit/', views.quit_game, name='quit'),
]