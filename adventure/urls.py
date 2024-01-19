from django.urls import path
from .views import start_page, explore_room

app_name = 'adventure'

urlpatterns = [
    path('', start_page, name='start_page'), 
    path('dungeon_adventure/<str:current_room>/', explore_room, name='explore_room'),
]
