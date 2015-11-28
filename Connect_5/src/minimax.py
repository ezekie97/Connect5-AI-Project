from src.heuristicFinder import *
from src.board import *
import copy

__author__ = 'Bill'


class MiniMax:
    """
    Apply the mini-max algorithm and use it to decide on the AI's moves.
    Assume AI is always max and human is always min.
    """

    def __init__(self, p1, p2):
        self.human = p1
        self.ai = p2
        self.heuristic_finder = HeuristicFinder(p1, self.ai)

    def mini_max(self, board, depth, max_node):
        """
        Perform minimax
        :param board: the current connect 5 board.
        :param depth: the depth of the tree.
        :param max_node: boolean value to determine whether we are at max or min node.
        :return: The next node to move to in the min_max tree
        """
        options = []
        if depth == 0:
            return [board, self.heuristic_finder.heuristic(board)]
        elif max_node:  # max
            for col in range(0, Board.get_length()):
                board_copy = copy.deepcopy(board)
                if board_copy.can_drop(col)[0]:
                    board_copy.drop(self.ai, col)
                    options.append(self.mini_max(board_copy, depth - 1, False))
            maximum = options[0][1]
            max_board = options[0][0]
            for j in range(1, len(options)):
                if options[j][1] > maximum:
                    maximum = options[j][1]
                    max_board = options[j][0]
            return [max_board, maximum]

        else:  # min
            for col in range(0, Board.get_length()):
                board_copy = copy.deepcopy(board)
                if board_copy.can_drop(col)[0]:
                    board_copy.drop(self.human, col)
                    options.append(self.mini_max(board_copy, depth - 1, True))
            minimum = options[0][1]
            min_board = options[0][0]
            for j in range(1, len(options)):
                if options[j][1] < minimum:
                    minimum = options[j][1]
                    min_board = options[j][0]
            return [min_board, minimum]
