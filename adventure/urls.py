# adventure/urls.py

from django.urls import path
from .views import intro, introScene, showShadowFigure

app_name = 'adventure'

urlpatterns = [
    path('intro/', intro, name='intro'),
    path('intro_scene/', introScene, name='intro_scene'),
    path('show_shadow_figure/', showShadowFigure, name='show_shadow_figure'),  # Add this line for showShadowFigure
    # Add other URL patterns as needed
]
