# pythonpractice/urls.py
from django.urls import path
from .views import print_example

app_name = 'pythonpractice'

urlpatterns = [
    path('print/', print_example, name='print_example'),
]
