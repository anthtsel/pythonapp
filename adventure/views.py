# views.py

from django.shortcuts import render

weapon = False

def strangeCreature(request):
    global weapon
    actions = ["fight", "flee"]
    context = {'current_scene': 'strange_creature'}

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').lower()

        if user_input in actions:
            if user_input == "fight":
                if weapon:
                    context['result'] = "You kill the ghoul with the knife you found earlier. After moving forward, you find one of the exits. Congrats!"
                    context['game_over'] = True
                else:
                    context['result'] = "The ghoul-like creature has killed you."
                    context['game_over'] = True
            elif user_input == "flee":
                return showSkeletons(request)
        else:
            context['error'] = "Please enter a valid option."

    return render(request, 'adventure/game.html', context)

def showSkeletons(request):
    global weapon
    directions = ["backward", "forward"]
    context = {'current_scene': 'show_skeletons'}

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').lower()

        if user_input in directions:
            if user_input == "left":
                context['found_knife'] = True
                weapon = True
            elif user_input == "backward":
                return introScene(request)
            elif user_input == "forward":
                return strangeCreature(request)
        else:
            context['error'] = "Please enter a valid option."

    return render(request, 'adventure/game.html', context)

# Define similar views for hauntedRoom, cameraScene, showShadowFigure, and introScene

def hauntedRoom(request):
    directions = ["right", "left", "backward"]
    context = {'current_scene': 'haunted_room'}

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').lower()

        if user_input in directions:
            if user_input == "right":
                context['result'] = "Multiple ghoul-like creatures start emerging as you enter the room. You are killed."
                context['game_over'] = True
            elif user_input == "left":
                context['result'] = "You made it! You've found an exit."
                context['game_over'] = True
            elif user_input == "backward":
                return introScene(request)
        else:
            context['error'] = "Please enter a valid option."

    return render(request, 'adventure/game.html', context)

# Define similar views for cameraScene, showShadowFigure, and introScene

from django.shortcuts import render, HttpResponseRedirect

from django.shortcuts import render, HttpResponseRedirect, reverse

def introScene(request):
    directions = {
        "left": showShadowFigure,
        "right": showSkeletons,
        "forward": hauntedRoom,
        "backward": intro,
    }
    context = {'current_scene': 'intro_scene'}

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').lower()
        print("Debug: user_input =", user_input)

        if user_input in directions:
            print(f"Debug: Going to {directions[user_input].__name__}")
            context['current_scene'] = user_input  # Update current_scene if needed
            return render(request, 'adventure/game.html', context)
        else:
            context['error'] = "Please enter a valid option."

    return render(request, 'adventure/game.html', context)


def showShadowFigure(request):
    directions = ["right", "backward"]
    context = {'current_scene': 'show_shadow_figure'}

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').lower()

        if user_input in directions:
            if user_input == "right":
                return cameraScene(request)
            elif user_input == "left":
                context['error'] = "You find that this door opens into a wall."
            elif user_input == "backward":
                return introScene(request)
        else:
            context['error'] = "Please enter a valid option."

    return render(request, 'adventure/game.html', context)

def cameraScene(request):
    directions = ["forward", "backward"]
    context = {'current_scene': 'camera_scene'}

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').lower()

        if user_input in directions:
            if user_input == "forward":
                context['result'] = "You made it! You've found an exit."
                context['game_over'] = True
            elif user_input == "backward":
                return showShadowFigure(request)
        else:
            context['error'] = "Please enter a valid option."

    return render(request, 'adventure/game.html', context)

def intro(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        return render(request, 'adventure/game.html', {'name': name, 'current_scene': 'intro_scene'})
    return render(request, 'adventure/game.html', {'current_scene': 'intro_scene'})
