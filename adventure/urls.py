# adventure/urls.py

from django.urls import path
from .views import introScene, showSkeletons, strangeCreature, hauntedRoom, cameraScene, showShadowFigure, intro

urlpatterns = [
    path('game/intro/', intro, name='intro'),
    path('game/introScene/', introScene, name='introScene'),
    path('game/show_skeletons/', showSkeletons, name='show_skeletons'),
    path('game/strange_creature/', strangeCreature, name='strange_creature'),
    path('game/haunted_room/', hauntedRoom, name='haunted_room'),
    path('game/camera_scene/', cameraScene, name='camera_scene'),
    path('game/show_shadow_figure/', showShadowFigure, name='show_shadow_figure'),
    # Add other URL patterns for additional scenes if needed
]
