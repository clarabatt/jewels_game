# Main Author: Izma Farooqui
# Main Reviewer:

def _check_if_both_has_same_signal(num1, num2):
        if num1 > 0 and num2 > 0:
            return True
        if num1 < 0 and num2 < 0:
            return True
        return False

# Part A: Evaluation Function
def evaluate_board(board, player):
    acc = 0
    for i, lines in enumerate(board):
        for j, cell in enumerate(lines):
            if _check_if_both_has_same_signal(player,board[i][j]):
                acc = acc + 1
    return acc
    
