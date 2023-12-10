# Main Author: Clara Verena Brito Battesini
# Main Reviewer:

from a3_parta import evaluate_board


# This function duplicates and returns the board. You may find this useful

def copy_board(board):
    current_board = []
    height = len(board)
    for i in range(height):
        current_board.append(board[i].copy())
    return current_board


class GameTree:
    class Node:
        def __init__(self, board, depth, player, tree_height=4):
            self.board = board
            self.depth = depth
            self.player = player
            self.tree_height = tree_height
            self.children = []
            self.score = None

    def __init__(self, board, player, tree_height=4):
        self.player = player
        self.board = copy_board(board)
        self.tree_height = tree_height
        self.root = self.Node(self.board, 0, self.player, self.tree_height)
        self.build_tree(self.root, 0)

    def build_tree(self, node, current_height):
        if current_height == self.tree_height:
            return
        for i in range(len(node.board)):
            for j in range(len(node.board[i])):
                if node.board[i][j] == 0:
                    new_board = copy_board(node.board)
                    new_board[i][j] = node.player
                    new_node = self.Node(
                        new_board,
                        current_height + 1,
                        node.player * -1,
                        self.tree_height,
                    )
                    node.children.append(new_node)
                    self.build_tree(new_node, current_height + 1)

    def get_move(self):
        height = len(self.board)
        width = len(self.board[0])
        if self.player == 1:
            return (0, 0)
        else:
            return (height - 1, width - 1)

    def _clear_tree_recursive(self, node):
        if node.children == []:
            return
        for child in node.children:
            self._clear_tree_recursive(child)
        node.children = []

    def clear_tree(self):
        self._clear_tree_recursive(self.root)
