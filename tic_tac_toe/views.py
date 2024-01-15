import random
import time
from django.shortcuts import render

# Initialize an empty board dictionary
board = {
    'top_L': ' ', 'top_M': ' ', 'top_R': ' ',
    'mid_L': ' ', 'mid_M': ' ', 'mid_R': ' ',
    'low_L': ' ', 'low_M': ' ', 'low_R': ' ',
}

user_marker = random.choice(['X', 'O'])
computer_marker = 'X' if user_marker == 'O' else 'O'

def update_board(position, marker):
    if board[position] == ' ':
        board[position] = marker

def get_current_board_state():
    return board

def get_computer_move():
    empty_positions = [pos for pos, marker in board.items() if marker == ' ']

    if empty_positions:
        return random.choice(empty_positions)
    else:
        return None

def tic_tac_toe(request):
    if ' ' in board.values() and computer_marker == 'X' and 'X' not in board.values():
        # Computer's move
        computer_position = get_computer_move()
        if computer_position:
            update_board(computer_position, computer_marker)
            current_turn = user_marker  # Switch to user's turn
    else:
        current_turn = user_marker if ' ' in board.values() else computer_marker
    
    # User's move
    if request.method == 'POST' and current_turn == user_marker:
        position = request.POST.get('position')
        update_board(position, user_marker)
        current_turn = computer_marker  # Switch to computer's turn

    # Computer's move
    if current_turn == computer_marker:
        computer_position = get_computer_move()
        if computer_position:
            time.sleep(1)  # Add a 1-second delay
            update_board(computer_position, computer_marker)
            current_turn = user_marker  # Switch to user's turn

    return render(request, 'tic_tac_toe/tic_tac_toe.html', {'board': get_current_board_state(), 'user_marker': user_marker, 'computer_marker': computer_marker, 'current_turn': current_turn})
