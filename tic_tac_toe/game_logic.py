# tic_tac_toe/game_logic.py

from random import choice

def initialize_board():
    return {'top-L': '', 'top-M': '', 'top-R': '', 'mid-L': '', 'mid-M': '', 'mid-R': '', 'low-L': '', 'low-M': '', 'low-R': ''}

def check_winner(board, turn):
    # Check rows, columns, and diagonals for a winner
    for row in ['top', 'mid', 'low']:
        if (board[f'{row}-L'] == board[f'{row}-M'] == board[f'{row}-R'] == turn):
            return True

    for col in ['L', 'M', 'R']:
        if (board[f'top-{col}'] == board[f'mid-{col}'] == board[f'low-{col}'] == turn):
            return True

    if (board['top-L'] == board['mid-M'] == board['low-R'] == turn) or \
       (board['top-R'] == board['mid-M'] == board['low-L'] == turn):
        return True

    return False

def is_board_full(board):
    return '' not in board.values()

def tic_tac_toe_logic(request, user_move=None):
    # Retrieve or initialize the board in the session
    if 'theBoard' not in request.session:
        request.session['theBoard'] = initialize_board()

    board = request.session['theBoard']
    user_turn = 'X'
    computer_turn = 'O'

    # Check if the game is already won or a tie
    if check_winner(board, user_turn) or check_winner(board, computer_turn) or is_board_full(board):
        # Reset the board if the game is over
        request.session['theBoard'] = initialize_board()

    # Process user move
    if user_move:
        if board[user_move] == '':
            board[user_move] = user_turn

            # Check if the user wins after their move
            if check_winner(board, user_turn):
                # Reset the board if the user wins
                request.session['theBoard'] = initialize_board()

            return board

    # Process computer move
    empty_spaces = [key for key, value in board.items() if value == '']
    if empty_spaces:
        computer_move = choice(empty_spaces)
        board[computer_move] = computer_turn

        # Check if the computer wins after its move
        if check_winner(board, computer_turn):
            # Reset the board if the computer wins
            request.session['theBoard'] = initialize_board()

    return board
