from django.shortcuts import render
from .hangman_art import stages
from game_logic.hangman_words import word_list
import random

# Initialize chosen_word outside the function
chosen_word = random.choice(word_list)


def play_hangman_game(request):
    # Access the global chosen_word
    global chosen_word

    # Initialize variables
    word_length = len(chosen_word)
    lives = 6
    display = ["_" for _ in range(word_length)]
    message = ""
    end_of_game = False

    # Initialize display_str here
    display_str = " ".join(display)

    if request.method == "POST":
        # Process the guess and update the game state
        guess = request.POST.get("guess", "").lower()
        display, lives, message, end_of_game = update_game_state(guess, chosen_word, display, lives, message, display_str)

    # Update display_str after processing the guess
    display_str = " ".join(display)

    # Check if the game is lost
    if lives == 0:
        message = "You lose."
        end_of_game = True

    # Render the template with the updated game state
    context = {
        "stages": stages[lives],
        "display": display_str,
        "message": message,
        "end_of_game": end_of_game,
    }

    return context


def update_game_state(guess, chosen_word, display, lives, message, display_str):
    end_of_game = False  # Initialize end_of_game variable

    if guess in display:
        message = f"You've already guessed {guess}"
    else:
        correct_guess = False
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                correct_guess = True

        if not correct_guess:
            message = f"You guessed {guess}, that's not in the word. You lose a life."
            lives -= 1
            if lives == 0:
                message = "You lose."
                end_of_game = True

    return display, lives, message, end_of_game
