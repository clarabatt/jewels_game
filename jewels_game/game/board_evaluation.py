def check_if_both_has_same_signal(num1, num2):
    if num1 > 0 and num2 > 0:
        return True
    if num1 < 0 and num2 < 0:
        return True
    return False


def evaluate_board(board, player):
    acc_opponent = 0

    acc = 0
    for i, lines in enumerate(board):
        for j, cell in enumerate(lines):
            if check_if_both_has_same_signal(player, board[i][j]):
                acc = acc + 1
            elif board[i][j] == 0:
                pass
            else:
                acc_opponent = acc_opponent + 1

    if acc_opponent == 0:
        acc = len(board)
        acc = acc*acc

    return acc
