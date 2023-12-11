# Main Author: Clara Verena Brito Battesini
# Main Reviewer:

from a1_partc import Queue
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
            self.move_coordinates = None
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

        # Generate all valid moves

        for i in range(len(node.board)):
            for j in range(len(node.board[i])):
                if node.board[i][j] == 0 or node.board[i][j] == depth_player:
                    new_board = copy_board(node.board)
                    new_board[i][j] += depth_player

                    the_queue = Queue()
                    overflow(new_board, the_queue)
                    new_node = self.Node(
                        new_board, new_depth, depth_player, self.tree_height
                    )
                    new_node.move_coordinates = (i, j)

                    node.children.append(new_node)

                    if not evaluate_board(new_board, self.player) == len(
                        new_board
                    ) * len(new_board):
                        self.build_tree(new_node, new_depth)

        if node.children:
            if node.player == self.player:
                node.score = max(child.score for child in node.children)
            else:
                node.score = min(child.score for child in node.children)

    def get_scores_by_depth(self, target_depth):
        if target_depth < 0:
            raise ValueError("Depth must be non-negative")

        queue = Queue()
        queue.enqueue((self.root, 0))
        scores_at_depth = []

        while not queue.is_empty():
            node, depth = queue.dequeue()

            if depth == target_depth:
                scores_at_depth.append(node.score)
            elif depth < target_depth:
                for child in node.children:
                    queue.enqueue((child, depth + 1))

        scores_at_depth.sort(reverse=True)
        return scores_at_depth

    def get_move(self):
        return self.get_scores_by_depth(self.tree_height - 1)[0].move_coordinates

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
