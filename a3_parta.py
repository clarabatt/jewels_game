# Main Author: Izma Farooqui
# Main Reviewer:

def overflow(board):
    same_sign = all(all(cell >= 0 for cell in row) or all(cell < 0 for cell in row) for row in board)
    if same_sign:
        return 1
    return 0


def evaluate_board(board, player):
    if check_winner(board, player):
        return float('inf') 
    elif check_winner(board, -player):
        return float('-inf')  
    else:
        player_pieces = sum(row.count(player) for row in board)
        opponent_pieces = sum(row.count(-player) for row in board)
        return player_pieces - opponent_pieces

def check_winner(board, player):
    player_pieces = sum(row.count(player) for row in board)
    opponent_pieces = sum(row.count(-player) for row in board)

    return player_pieces > opponent_pieces
