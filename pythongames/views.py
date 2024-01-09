from django.shortcuts import render, get_object_or_404, redirect
from .models import HangmanGame
from .word_list import words
import random

def new_game(request):
    word = random.choice(words)
    game = HangmanGame.objects.create(word=word)
    return redirect('pythongames:hangman', game_id=game.id)

def hangman_game(request, game_id):
    game = get_object_or_404(HangmanGame, id=game_id)

    if request.method == 'POST':
        guessed_letter = request.POST.get('guessed_letter').lower()

        if guessed_letter.isalpha() and guessed_letter not in game.guessed_letters:
            game.guessed_letters += guessed_letter

            if guessed_letter not in game.word:
                game.attempts_left -= 1

            game.save()

    context = {
        'game': game,
        'game_over': game.attempts_left == 0 or '_' not in game.display_word(),
    }

    return render(request, 'pythongames/hangman.html', context)
