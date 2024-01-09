# pythongames/urls.py
from django.urls import path
from .views import new_game, hangman_game

app_name = 'pythongames'

urlpatterns = [
    path('new/', new_game, name='new_game'),
    path('hangman/<int:game_id>/', hangman_game, name='hangman'),
]