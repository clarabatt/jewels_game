from ..algo.queue import Queue
from ..algo.overflow import get_overflow_list, overflow
from .board_evaluation import evaluate_board, check_if_both_has_same_signal


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
            self.move_coordinates = None
            self.player = player
            self.tree_height = tree_height
            self.children = []
            self.score = None

        def is_game_over(self):
            """
            Returns True if the game is over, False otherwise
            """
            if evaluate_board(self.board, self.player) == len(self.board) * len(
                self.board[0]
            ):
                return True
            else:
                return False

    def __init__(self, board, player, tree_height=4):
        """
        Tree constructor, creates the root node and builds the tree
        """
        self.player = player
        self.board = copy_board(board)
        self.choice = None
        self.tree_height = tree_height
        self.root = self.Node(self.board, 0, self.player, self.tree_height)
        self.build_tree(self.root, 0)

    def build_tree(self, node, current_depth):
        """
        Builds the tree recursively creating child nodes for each possible state resulting from the overflow mechanic and alternates between players at each level of the tree.
        Each leaf node is assigned a score based on the evaluate_board function.
        """

        if current_depth == 0:
            depth_player = node.player
        else:
            depth_player = node.player * -1

        new_depth = current_depth + 1
        max_score = len(node.board) * len(node.board[0])

        if current_depth >= self.tree_height:
            node.score = evaluate_board(node.board, self.player) * depth_player
            return

        # Generate all valid moves

        for i in range(len(node.board)):
            for j, cell in enumerate(node.board[i]):
                if cell == 0 or check_if_both_has_same_signal(cell, depth_player):
                    new_board = copy_board(node.board)

                    new_board[i][j] = new_board[i][j] + depth_player

                    is_overflow_possible = get_overflow_list(new_board)

                    # Perform the overflow and repopulate the new_board
                    if is_overflow_possible:
                        overflow_result = Queue()
                        overflow(new_board, overflow_result)
                        while overflow_result.size > 1:
                            dequed_element = 0
                            dequed_element = overflow_result.dequeue()
                        new_board = overflow_result.dequeue()

                    new_node = self.Node(
                        new_board, new_depth, depth_player, node.tree_height - 1
                    )
                    new_node.score = evaluate_board(new_board, self.player)
                    new_node.move_coordinates = (i, j)
                    node.children.append(new_node)
                    if new_depth < self.tree_height - 1:
                        if not new_node.score == max_score:
                            self.build_tree(new_node, new_depth)

    def minimax(self, node, depth, is_maximizing_player):
        """
        Minimax algorithm implementation
        """
        if node.is_game_over():
            return node

        depth += 1
        possible_moves = []

        for childen_node in node.children:
            possible_moves.append(childen_node)

        if not is_maximizing_player:
            # if the player is maximizing, return the maximum score
            possible_moves.sort(key=lambda node: node.score, reverse=True)
            self.choice = possible_moves[0].move_coordinates
            return possible_moves[0]

        else:
            # if the player is minimizing, return the minimum score
            possible_moves.sort(key=lambda node: node.score)
            self.choice = possible_moves[0].move_coordinates
            return possible_moves[0]

    def get_move(self):
        """
        Returns the move that the bot should make
        """
        self.minimax(self.root, 0, False)
        return self.choice

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
