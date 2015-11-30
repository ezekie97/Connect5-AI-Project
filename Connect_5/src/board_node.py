__author__ = 'Bill'


class BoardNode:
    """
    Nodes used in the Minimax algorithm. Each node contains a board, a heuristic value,
    and zero or more children.
    """

    def __init__(self, board, heuristic):
        """
        Create a BoardNode for the minimax algorithm
        :param board: this node's board.
        :param heuristic: this node's heuristic value
        """
        self.board = board
        self.heuristic = heuristic

    def get_board(self):
        """
        :return: this node's board
        """
        return self.board

    def get_heuristic(self):
        """
        :return: this node's heuristic
        """
        return self.heuristic

    def set_heuristic(self, h):
        """
        Set a new heuristic value
        :param h: the new heuristic value
        """
        self.heuristic = h
