__author__ = "Bill"

from src.board import *


class HeuristicFinder:
    """
    Used to find heuristic values of a Connect 5 Game Board
    """

    def __init__(self, human_player, ai_player):

        self.ai_player = ai_player
        self.human_player = human_player

    def heuristic(self, board):
        """
        Find the heuristic value of a Connect 5 board.
        :param board: A Connect 5 Board object.
        :return: a number representing the heuristic value.
            Special Values:
                1000 - Board where AI wins.
                -1000 - Board where AI loses.
                0  - Tie
        """
        if board.is_filled():
            return 0
        elif board.find_winner() == self.ai_player:  # AI Wins
            return 10000
        elif board.find_winner() == self.human_player:  # AI Loses
            return -10000
        else:
            ai_four_in_row = board.find_n_in_a_row(self.ai_player, 4)
            ai_three_in_row = board.find_n_in_a_row(self.ai_player, 3)
            ai_two_in_row = board.find_n_in_a_row(self.ai_player, 2)

            human_four_in_row = board.find_n_in_a_row(self.human_player, 4)
            human_three_in_row = board.find_n_in_a_row(self.human_player, 3)
            human_two_in_row = board.find_n_in_a_row(self.human_player, 2)

            heuristic = 100 * ai_four_in_row + 10 * ai_three_in_row + 0.5 * ai_two_in_row
            heuristic -= 100 * human_four_in_row + 10 * human_three_in_row + 0.5 * human_two_in_row

            bonus = 0
            center = board.piece_at(6,4)
            left_corner = board.piece_at(6,0)
            right_corner = board.piece_at(6,8)
            if self.ai_player == center:  # center
                bonus += 50
            elif self.human_player == center:
                bonus -= 50

            if self.ai_player == left_corner:  # center
                bonus += 15
            elif self.human_player == left_corner:
                bonus -= 15

            if self.ai_player == right_corner:  # center
                bonus += 15
            elif self.human_player == right_corner:
                bonus -= 15

            heuristic += bonus

            #print("Heuristic")
            #print(heuristic)
            return heuristic
