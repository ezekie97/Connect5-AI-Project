__author__ = 'Bill'


class BoardNode:
    """
    Nodes used in the Minimax algorithm
    """

    def __init__(self, board, heuristic):
        """
        """
        self.board = board
        self.heuristic = heuristic
        self.children = []

    def get_board(self):
        return self.board

    def get_heuristic(self):
        return self.heuristic

    def get_type(self):
        return self.type

    def has_children(self):
        return len(self.children) != 0

    def get_children(self):
        return self.children

    def add_child(self, child):
        self.children.append(child)

    def set_heuristic(self,h):
        self.heuristic = h