# Main Author: Izma Farooqui
# Main Reviewer:

# A1 overflow function modification
def overflow(board):
    same_sign = all(all(cell >= 0 for cell in row) or all(cell < 0 for cell in row) for row in board)
    if same_sign:
        return 1
    return 0

# Part A: Evaluation Function
def evaluate_board(board, player):
    if check_winner(board, player):
        return float('inf')  # The player wins
    elif check_winner(board, -player):
        return float('-inf')  # The opponent wins
    else:
        player_pieces = sum(row.count(player) for row in board)
        opponent_pieces = sum(row.count(-player) for row in board)
        return player_pieces - opponent_pieces

def check_winner(board, player):
    player_pieces = sum(row.count(player) for row in board)
    opponent_pieces = sum(row.count(-player) for row in board)

    # Player wins if they have more pieces than the opponent
    return player_pieces > opponent_pieces
