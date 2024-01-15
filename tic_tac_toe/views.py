import random
import time
from django.shortcuts import render, redirect

# Initialize an empty board dictionary
board = {
    'top_L': ' ', 'top_M': ' ', 'top_R': ' ',
    'mid_L': ' ', 'mid_M': ' ', 'mid_R': ' ',
    'low_L': ' ', 'low_M': ' ', 'low_R': ' ',
}

# Initialize user and computer markers and the initial turn
user_marker = None
computer_marker = None
current_turn = None

def initialize_game():
    global user_marker, computer_marker, current_turn
    user_marker = random.choice(['X', 'O'])
    computer_marker = 'X' if user_marker == 'O' else 'O'
    current_turn = user_marker if user_marker == 'X' else computer_marker

initialize_game()

def update_board(position, marker):
    if board[position] == ' ':
        board[position] = marker

def get_current_board_state():
    return board

def get_computer_move():
    # Check if computer can win in the next move
    for pos in board.keys():
        if board[pos] == ' ':
            board[pos] = computer_marker
            if check_winner() == computer_marker:
                board[pos] = ' '  # Undo the move
                return pos

            board[pos] = ' '  # Undo the move

    # Check if user can win in the next move and block them
    for pos in board.keys():
        if board[pos] == ' ':
            board[pos] = user_marker
            if check_winner() == user_marker:
                board[pos] = computer_marker  # Block the user
                return pos

            board[pos] = ' '  # Undo the move

    # If no immediate win/loss, choose a random move
    empty_positions = [pos for pos, marker in board.items() if marker == ' ']

    if empty_positions:
        return random.choice(empty_positions)
    else:
        return None

def check_winner():
    # Check rows, columns, and diagonals for a win
    for row in ['top', 'mid', 'low']:
        if board[f'{row}_L'] == board[f'{row}_M'] == board[f'{row}_R'] != ' ':
            return board[f'{row}_L']  # Return the winning marker

    for col in ['L', 'M', 'R']:
        if board[f'top_{col}'] == board[f'mid_{col}'] == board[f'low_{col}'] != ' ':
            return board[f'top_{col}']  # Return the winning marker

    if board['top_L'] == board['mid_M'] == board['low_R'] != ' ':
        return board['top_L']  # Return the winning marker

    if board['top_R'] == board['mid_M'] == board['low_L'] != ' ':
        return board['top_R']  # Return the winning marker

    return None  # No winner

def tic_tac_toe(request):
    global current_turn

    # User's move
    if request.method == 'POST' and current_turn == user_marker:
        position = request.POST.get('position')
        update_board(position, user_marker)

        # Check for a winner after user's move
        winner = check_winner()
        if winner:
            return render(request, 'tic_tac_toe/tic_tac_toe.html', {'board': get_current_board_state(), 'user_marker': user_marker, 'computer_marker': computer_marker, 'current_turn': current_turn, 'winner': winner})

        current_turn = computer_marker  # Switch to computer's turn

    # Computer's move
    if current_turn == computer_marker:
        computer_position = get_computer_move()
        if computer_position:
            time.sleep(1)  # Add a 1-second delay
            update_board(computer_position, computer_marker)

        # Check for a winner after computer's move
        winner = check_winner()
        if winner:
            return render(request, 'tic_tac_toe/tic_tac_toe.html', {'board': get_current_board_state(), 'user_marker': user_marker, 'computer_marker': computer_marker, 'current_turn': current_turn, 'winner': winner})

        current_turn = user_marker  # Switch to user's turn

    return render(request, 'tic_tac_toe/tic_tac_toe.html', {'board': get_current_board_state(), 'user_marker': user_marker, 'computer_marker': computer_marker, 'current_turn': current_turn, 'winner': None})

def play_again(request):
    global board, user_marker, computer_marker, current_turn
    board = {
        'top_L': ' ', 'top_M': ' ', 'top_R': ' ',
        'mid_L': ' ', 'mid_M': ' ', 'mid_R': ' ',
        'low_L': ' ', 'low_M': ' ', 'low_R': ' ',
    }
    initialize_game()  # Reinitialize user_marker, computer_marker, and current_turn
    return redirect('tic_tac_toe:tic_tac_toe')