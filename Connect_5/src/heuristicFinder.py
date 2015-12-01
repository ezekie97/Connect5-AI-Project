__author__ = "Bill"


class HeuristicFinder:
    """
    Used to find heuristic values of a Connect 5 Game Board
    """

    def __init__(self, human_player, ai_player):
        """
        Create a HeurisiticFinder object.
        :param human_player: the piece value for the human player
        :param ai_player: the piece value for the ai player
        """
        self.ai_player = ai_player
        self.human_player = human_player

    def heuristic(self, board):
        """
        Find the heuristic value of a Connect 5 board.
        :param board: A Connect 5 Board object.
        :return: a number representing the heuristic value.
            Special Values:
                10000 - Board where AI wins.
                -10000 - Board where AI loses.
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

            # Number of potential wins that can happen if one of the players fills in a blank spot
            # between 4 or more of its own pieces.
            ai_unconnected_wins = board.find_disconnected_wins(self.ai_player)
            human_unconnected_wins = board.find_disconnected_wins(self.human_player)

            ai_threats = ai_four_in_row + ai_unconnected_wins
            human_threats = human_four_in_row + human_unconnected_wins

            heuristic = 50 * ai_threats + 10 * ai_three_in_row + 0.5 * ai_two_in_row
            heuristic -= 50 * human_threats + 10 * human_three_in_row + 0.5 * human_two_in_row

            bonus = 0

            # Values for center and corners, vital pieces
            center = board.piece_at(6, 4)
            left_corner = board.piece_at(6, 0)
            right_corner = board.piece_at(6, 8)

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
            return heuristic
