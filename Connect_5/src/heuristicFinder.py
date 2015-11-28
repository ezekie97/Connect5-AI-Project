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
                -150 - Board where AI wins.
                -150 - Board where AI loses.
                - 0  - Tie
        """
        if board.is_filled():
            return 0
        elif board.find_winner() == self.ai_player:  # AI Wins
            return 1000
        elif board.find_winner() is not None:
            return -1000
        else:
            ai_four_in_row = board.find_n_in_a_row(self.ai_player, 4)
            ai_three_in_row = board.find_n_in_a_row(self.ai_player, 3)
            ai_two_in_row = board.find_n_in_a_row(self.ai_player, 2)

            human_four_in_row = board.find_n_in_a_row(self.human_player, 4)
            human_three_in_row = board.find_n_in_a_row(self.human_player, 3)
            human_two_in_row = board.find_n_in_a_row(self.human_player, 2)

            #print("Human")

            #print([self.human_player, human_four_in_row, human_three_in_row, human_two_in_row])
            #print("AI")
            #print([self.ai_player, ai_four_in_row, ai_three_in_row, ai_two_in_row])

            heuristic =  7 * ai_four_in_row + 3 * ai_three_in_row + ai_two_in_row
            heuristic -= 7 * human_four_in_row + 3 * human_three_in_row + human_two_in_row

            bonus = 0
            if self.ai_player == board.piece_at(6, 4):  # center
                bonus += 5
            elif self.ai_player == board.piece_at(6, 0) or self.ai_player == board.piece_at(6, 8):
                bonus += 2
            heuristic += bonus

            #print("Heuristic")
            #print(heuristic)
            return heuristic
