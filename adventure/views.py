# adventure/views.py

from django.shortcuts import render
from django.urls import reverse

# adventure/views.py

from django.shortcuts import render

def intro(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        return render(request, 'adventure/game.html', {'name': name, 'current_scene': 'intro_scene'})
    return render(request, 'adventure/intro.html')


def introScene(request):
    directions = {
        "left": reverse('adventure:show_shadow_figure'),  # Redirect to the show_shadow_figure view
    }
    context = {'current_scene': 'intro_scene'}

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').lower()

        if user_input in directions:
            context['current_scene'] = user_input
            return render(request, 'adventure/game.html', context)
        else:
            context['error'] = "Please enter a valid option."

    return render(request, 'adventure/game.html', context)

def showShadowFigure(request):
    context = {'current_scene': 'show_shadow_figure'}

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').lower()

        # Process user input for the show_shadow_figure scene
        # Add your logic here based on user input

    return render(request, 'adventure/game.html', context)
