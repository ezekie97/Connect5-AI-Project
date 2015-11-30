from src.board_node import *

__author__ = 'Bill'


class MinBoardNode(BoardNode):
    """
    Nodes used in the Minimax algorithm. Each node contains a board, a heuristic value,
    and zero or more children.
    """

    def __init__(self, board, heuristic, beta, parent=None):
        """
        Create a BoardNode for the minimax algorithm
        :param board: this node's board.
        :param heuristic: this node's heuristic value
        :param alpha: this max_node's alpha value.
        """
        BoardNode.__init__(self, board, heuristic,parent)
        self.beta = beta

    def get_beta(self):
        return self.beta

    def set_beta(self, b):
        self.beta = b
