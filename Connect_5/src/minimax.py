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

    def __init__(self, p1, p2):
        """
        Set up the minimax algorithm
        :param p1: the piece vlue for the human player.
        :param p2: the piece value for the ai.
        """
        self.human = p1
        self.ai = p2
        self.heuristic_finder = HeuristicFinder(p1, self.ai)

    def mini_max(self, board, depth, max_node):
        """
        Perform minimax
        :param board: the current connect 5 board.
        :param depth: the depth of the tree.
        :param max_node: boolean value to determine whether we are at max or min node.
        :return: The next node to move to in the min_max tree after the entire algorithm is complete.
        """
        if depth == 0:
            return BoardNode(board, self.heuristic_finder.heuristic(board))
        elif max_node:  # max
            parent = BoardNode(board, 0)
            for col in range(0, Board.get_length()):
                board_copy = copy.deepcopy(board)
                if board_copy.can_drop(col)[0]:
                    board_copy.drop(self.ai, col)
                    parent.add_child(
                        BoardNode(board_copy, self.mini_max(board_copy, depth - 1, False).get_heuristic()))
            children = parent.get_children()
            maximum = children[0].get_heuristic()
            child_pos = 0
            for i in range(1, len(children)):
                if children[i].get_heuristic() > maximum:
                    maximum = children[i].get_heuristic()
                    child_pos = i
            return BoardNode(children[child_pos].get_board(), maximum)
        else:  # min
            parent = BoardNode(board, 0)
            for col in range(0, Board.get_length()):
                board_copy = copy.deepcopy(board)
                if board_copy.can_drop(col)[0]:
                    board_copy.drop(self.human, col)
                    parent.add_child(
                        BoardNode(board_copy, self.mini_max(board_copy, depth - 1, True).get_heuristic()))
            children = parent.get_children()
            minimum = children[0].get_heuristic()
            child_pos = 0
            for i in range(1, len(children)):
                if children[i].get_heuristic() < minimum:
                    minimum = children[i].get_heuristic()
                    child_pos = i
            return BoardNode(children[child_pos].get_board(), minimum)
