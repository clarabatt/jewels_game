# Main Author: Clara Verena Brito Battesini
# Main Reviewer:

from a1_partd import get_overflow_list, overflow
from a3_parta import evaluate_board


def copy_board(board):
    """
    This function duplicates and returns the board
    """
    current_board = []
    height = len(board)
    for i in range(height):
        current_board.append(board[i].copy())
    return current_board


class GameTree:
    """
    Decision Tree class for the game
    """

    class Node:
        """
        Node class for the GameTree class
        """

        def __init__(self, board, depth, player, tree_height=4):
            """
            Node class constructor, empty children list and score
            """
            self.board = board
            self.depth = depth
            self.player = player
            self.tree_height = tree_height
            self.children = []
            self.score = None

    def __init__(self, board, player, tree_height=4):
        """
        Tree constructor, creates the root node and builds the tree
        """
        self.player = player
        self.board = copy_board(board)
        self.tree_height = tree_height
        self.root = self.Node(self.board, 0, self.player, self.tree_height)
        self.build_tree(self.root, 0)

    def build_tree(self, node, current_depth):
        """
        Builds the tree recursively creating child nodes for each possible state resulting from the overflow mechanic and alternates between players at each level of the tree.
        Each leaf node is assigned a score based on the evaluate_board function.
        """
        depth_player = node.player
        new_depth = current_depth + 1

        if (new_depth % 2) == 0:
            depth_player = node.player * -1

        if current_depth >= self.tree_height:
            node.score = evaluate_board(node.board, self.player)
            return

        overflow_cells = get_overflow_list(node.board)

        for cell in overflow_cells:
            new_board = copy_board(node.board)
            overflow(new_board, cell)
            new_node = self.Node(new_board, new_depth, depth_player, self.tree_height)
            node.children.append(new_node)
            self.build_tree(new_node, new_depth)

    def get_move(self):
        height = len(self.board)
        width = len(self.board[0])
        if self.player == 1:
            return (0, 0)
        else:
            return (height - 1, width - 1)

    def _clear_tree_recursive(self, node):
        """
        Helper function that clears the tree recursively
        """
        if node.children == []:
            return
        for child in node.children:
            self._clear_tree_recursive(child)
        node.children = []

    def clear_tree(self):
        """
        Clears the tree trigger function
        """
        self._clear_tree_recursive(self.root)
