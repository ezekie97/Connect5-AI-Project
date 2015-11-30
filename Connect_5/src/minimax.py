from src.heuristicFinder import *
from src.board import *
from src.board_node import *
import copy

__author__ = 'Bill'


class MiniMax:
    """
    Apply the mini-max algorithm and use it to decide on the AI's moves.
    Assume AI is always max and human is always min.
    """

    # Class constants
    INF = float("inf")  # infinity
    NEG_INF = - float("inf")  # -infinity

    def __init__(self, p1, p2):
        """
        Set up the minimax algorithm
        :param p1: the piece vlue for the human player.
        :param p2: the piece value for the ai.
        """
        self.human = p1
        self.ai = p2
        self.heuristic_finder = HeuristicFinder(p1, self.ai)

    def mini_max(self, node, alpha, beta, depth):
        """
        MiniMax algorithm with alpha-beta pruning.
        :param node: the current Max or Min Board Node
        :param alpha: the alpha value
        :param beta: the beta value
        :param depth: the depth of the search.
        :return: the node which represents the next best move to make.
        """
        # Depth is assumed to be > 0.
        node_board = node.get_board()
        maximum = self.NEG_INF
        best = None
        for col in range(0, Board.get_length()):
            if node_board.can_drop(col):
                board_copy = copy.deepcopy(node_board)
                board_copy.drop(self.ai, col)
                min_node = BoardNode(board_copy, self.INF)
                child = self.mini_max_min(min_node, alpha, beta, depth - 1)
                ch = child.get_heuristic()
                if ch > maximum:
                    maximum = ch
                    best = min_node
                    alpha = max(alpha, ch)
                    if beta <= alpha:
                        break
        return best

    def mini_max_min(self, node, alpha, beta, depth):
        """
        MiniMax algorithm with alpha-beta pruning. Min Node Handling
        :param node: the current Max or Min Board Node
        :param alpha: the alpha value
        :param beta: the beta value
        :param depth: the depth of the search.
        :return: the node which represents the next best move to make for the human.
        """
        if depth == 0 or node.get_board().find_winner() is not None:
            node.set_heuristic(self.heuristic_finder.heuristic(node.get_board()))
            return node
        else:
            # Depth is assumed to be > 0.
            node_board = node.get_board()
            minimum = self.INF
            best = None
            for col in range(0, Board.get_length()):
                if node_board.can_drop(col):
                    board_copy = copy.deepcopy(node_board)
                    board_copy.drop(self.human, col)
                    max_node = BoardNode(board_copy, self.NEG_INF)
                    child = self.mini_max_max(max_node, alpha, beta, depth - 1)
                    ch = child.get_heuristic()
                    if ch < minimum:
                        minimum = ch
                        best = max_node
                        best.set_heuristic(minimum)
                        beta = min(beta, ch)
                        if beta <= alpha:
                            break
            return best

    def mini_max_max(self, node, alpha, beta, depth):
        """
        MiniMax algorithm with alpha-beta pruning. Max Node Hanlding
        :param node: the current Max or Min Board Node
        :param alpha: the alpha value
        :param beta: the beta value
        :param depth: the depth of the search.
        :return: the node which represents the next best move to make for the ai.
        """
        if depth == 0 or node.get_board().find_winner() is not None:
            node.set_heuristic(self.heuristic_finder.heuristic(node.get_board()))
            return node
        else:
            node_board = node.get_board()
            maximum = self.NEG_INF
            best = None
            for col in range(0, Board.get_length()):
                if node_board.can_drop(col):
                    board_copy = copy.deepcopy(node_board)
                    board_copy.drop(self.ai, col)
                    min_node = BoardNode(board_copy, self.INF)
                    child = self.mini_max_min(min_node, alpha, beta, depth - 1)
                    ch = child.get_heuristic()
                    if ch > maximum:
                        maximum = ch
                        best = min_node
                        best.set_heuristic(maximum)
                        alpha = max(alpha, ch)
                        if beta <= alpha:
                            break
            return best
