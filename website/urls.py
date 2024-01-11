from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pythongames/', include('pythongames.urls', namespace='pythongames')),
    path('pythonpractice/', include('pythonpractice.urls', namespace='pythonpractice')),
    path('adventure/', include('adventure.urls')),
    # Add other URLs as needed
]
