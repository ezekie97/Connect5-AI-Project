from src.board_node import *

__author__ = 'Bill'


class MaxBoardNode(BoardNode):
    """
    Nodes used in the Minimax algorithm. Each node contains a board, a heuristic value,
    and zero or more children.
    """

    def __init__(self, board, heuristic, alpha, parent=None):
        """
        Create a BoardNode for the minimax algorithm
        :param board: this node's board.
        :param heuristic: this node's heuristic value
        :param alpha: this max_node's alpha value.
        """
        BoardNode.__init__(self, board, heuristic, parent)
        self.alpha = alpha

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, a):
        self.alpha = a
