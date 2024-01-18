from django.urls import path
from .views import start_page, dungeon_adventure

app_name = 'adventure'

urlpatterns = [
    path('start_page/', start_page, name='start_page'),
    path('dungeon_adventure/', dungeon_adventure, name='dungeon_adventure'),
]
