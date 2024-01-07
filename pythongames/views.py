# pythongames/views.py
from django.shortcuts import render
from game_logic.hangman_main import play_hangman_game

def hangman(request):
    hangman_result = play_hangman_game(request)
    return render(request, 'pythongames/hangman.html', {'hangman_result': hangman_result})

def restart_game(request):
    # Add logic to restart the game
    return render(request, 'pythongames/restart.html')  # Create a new template for restarting

def quit_game(request):
    # Add logic to quit the game and generate a new word
    return render(request, 'pythongames/quit.html')  # Create a new template for quitting
