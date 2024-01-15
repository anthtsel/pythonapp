from django.urls import path
from .views import tic_tac_toe, play_again

app_name = 'tic_tac_toe'

urlpatterns = [
    path('tic_tac_toe/', tic_tac_toe, name='tic_tac_toe'),
    path('play_again/', play_again, name='play_again'),
]
