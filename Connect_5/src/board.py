__author__ = 'Bill'


class Board:
    """
    Class for the Connect 5 Game Board. The Board is always a 7 long by
    9 high.
    """

    # Class Constants
    BLANK_SPACE = "_"
    PLAYER_ONE = "R"  # Red Chip
    PLAYER_TWO = "B"  # Black Chip
    BOARD_HEIGHT = 7
    BOARD_LENGTH = 9
    SCORE_TO_WIN = 5

    def __init__(self):
        """
        Create a new board.
        """
        self.grid = self.create_grid()
        self.last_move = None

    def piece_at(self, row, col):
        """
        Get the player piece (or blank) at the specified location.
        :param row: specified row
        :param col: specified column
        :return: the value of the piece at row 'row' and column 'col'.
        """
        return self.grid[col][row]

    def can_drop(self, col_num):
        """
        :param col_num: the column number .
        :return: An array containing a boolean and an integer. The boolean is used to determine
            if a piece can be dropped and the integer is used to tell which row the piece will be dropped into.
        """
        blank_found = False
        row_num = self.BOARD_HEIGHT - 1
        while not blank_found and row_num >= 0:
            if self.grid[col_num][row_num] is not self.BLANK_SPACE:
                row_num -= 1
            else:
                blank_found = True
        return [blank_found, row_num]

    def drop(self, dropped_char, col_num):
        """
        Drop a piece into a column. If a piece cannot be dropped in a column, the player will
        be notified.
        :param dropped_char: the character of the player dropping the piece
        :param col_num: the column to drop a piece into.
        :return: true if the drop was successful.
        """
        drop = self.can_drop(col_num)
        can_drop = drop[0]
        row_num = drop[1]
        if can_drop:
            self.grid[col_num][row_num] = dropped_char
            self.last_move = [dropped_char, col_num, row_num]

    def is_filled(self):
        """
        :return: true if there are no blank spaces on the board.
        """
        blank_found = False
        for i in range(0, self.BOARD_HEIGHT):
            if blank_found:
                break
            for j in range(0, self.BOARD_LENGTH):
                if blank_found:
                    break
                if self.grid[j][i] == self.BLANK_SPACE:
                    blank_found = True
        return not blank_found

    def find_n_in_a_row(self, piece, n):
        """
        Find the number of times on the board where there are N adjacent
        non-blank pieces of the same type on the board.
        :param piece: the type of the piece.
        :param n: Look for n in_a_row
        :return: the number of n in_a_row for the specific piece on this board.
        """
        count = 0
        for row in range(0, Board.get_height()):
            for col in range(0, Board.get_length()):
                current_piece = self.grid[col][row]
                if current_piece == piece:
                    count += self.num_n_in_a_row_horizontal(row, col, current_piece, n)  # 0 or 1
                    count += self.num_n_in_a_row_vertical(row, col, current_piece, n)  # 0 or 1
                    count += self.num_n_in_a_row_diagonal(row, col, current_piece, n)  # 0, 1,  or 2
        return count

    def num_n_in_a_row_horizontal(self, row, col, piece, n):
        """
        Find the number of times on the board where there are N adjacent non-blank
        pieces of the same type in a horizontal line on the board.
        :param row: the row number of the piece
        :param col: the column number of the piece
        :param piece: the type of the piece
        :param n: Look for n_in_a_row
        :return: the number of times this piece satisfies the n_in_a_row condition horizontally. (Either 0 or 1)
        """
        streak = 0
        for curr_col in range(col, col + n):  # count the initial piece automatically
            if curr_col > Board.get_length() - 1:  # check out of bounds
                break
            if self.grid[curr_col][row] != piece:
                return 0
            else:
                streak += 1
        if streak == n:
            return 1
        else:
            return 0

    def num_n_in_a_row_vertical(self, row, col, piece, n):
        """
        Find the number of times on the board where there are N adjacent non-blank
        pieces of the same type in a vertical line on the board.
        :param row: the row number of the piece
        :param col: the column number of the piece
        :param piece: the type of the piece
        :param n: Look for n_in_a_row
        :return: the number of times this piece satisfies the n_in_a_row condition vertically. (Either 0 or 1)
        """
        streak = 0
        for curr_row in range(row - n + 1, row + 1):  # count the initial piece automatically
            if curr_row < 0:  # check out of bounds
                break
            if self.grid[col][curr_row] != piece:
                return 0
            else:
                streak += 1
        if streak == n:
            return 1
        else:
            return 0

    def num_n_in_a_row_diagonal(self, row, col, piece, n):
        """
        Find the number of times on the board where there are N adjacent non-blank
        pieces of the same type in a diagonal line on the board.
        :param row: the row number of the piece
        :param col: the column number of the piece
        :param piece: the type of the piece
        :param n: Look for n_in_a_row
        :return: the number of times this piece satisfies the n_in_a_row condition diagonally. (Either 0, 1, or 2)
        """
        result = 0
        streak = 0
        for modifier in range(0, n):  # count the initial piece automatically
            curr_col = col + modifier
            curr_row = row - modifier
            if curr_col > Board.get_length() - 1 or curr_row < 0:  # check out of bounds
                break
            if self.grid[curr_col][curr_row] != piece:
                return 0
            else:
                streak += 1
        if streak == n:
            result += 1

        streak = 0  # reset streak

        for modifier in range(0, n):  # count the initial piece automatically
            curr_col = col - modifier
            curr_row = row - modifier
            if curr_col < 0 or curr_row < 0:  # check out of bounds
                break
            if self.grid[curr_col][curr_row] != piece:
                return 0
            else:
                streak += 1
        if streak == n:
            result += 1

        return result

    def find_winner(self):
        """
        Check if the latest move created a victory.
        :return: a character representing a player, or None if there is no winner.
        """
        win_amount = self.SCORE_TO_WIN
        if self.find_n_in_a_row(Board.PLAYER_ONE, win_amount) >= 1:
            return Board.PLAYER_ONE
        elif self.find_n_in_a_row(Board.PLAYER_TWO, win_amount) >= 1:
            return Board.PLAYER_TWO
        else:
            return None

    def create_grid(self):
        """
        :return: the game grid.
        """
        grid = []
        for i in range(0, self.BOARD_LENGTH):
            grid.append(self.create_empty_column())
        return grid

    def get_last_move(self):
        return self.last_move

    def __str__(self):
        """
        :return: a string representation of the board.
        """
        board_string = ""
        for i in range(0, self.BOARD_HEIGHT):
            for j in range(0, self.BOARD_LENGTH):
                board_string += " " + self.grid[j][i] + " "
            board_string += "\n"
        return board_string

    def create_empty_column(self):
        """
        :return: an array representing an empty column on the board.
        """
        column = []
        for i in range(0, self.BOARD_HEIGHT):
            column.append(self.BLANK_SPACE)
        return column

    @staticmethod
    def get_length():
        """
        :return: the length of this board.
        """
        return Board.BOARD_LENGTH

    @staticmethod
    def get_height():
        """
        :return: the height of this board.
        """
        return Board.BOARD_HEIGHT

        # def get_threats(self):
        #     """
        #     :return: the dictionary containing all threats on the board.
        #     """
        #     return self.threats
        #
        # def get_player_one_even_threats(self):
        #     """
        #     :return: the number of even threats for player one
        #     """
        #     return self.threats["1E"]
        #
        # def get_player_one_odd_threats(self):
        #     """
        #     :return: the number of odd threats for player one
        #     """
        #     return self.threats["1O"]
        #
        # def get_player_two_even_threats(self):
        #     """
        #     :return: the number of even threats for player two
        #     """
        #     return self.threats["2E"]
        #
        # def get_player_two_odd_threats(self):
        #     """
        #     :return: the number of odd threats for player two
        #     """
        #     return self.threats["2O"]

        # def assess_threats(self):
        #     p1_even_threats = 0
        #     p1_odd_threats = 0
        #     p2_even_threats = 0
        #     p2_odd_threats = 0
        #     for row in range(0, Board.get_height()):
        #         for col in range(0, Board.get_length()):
        #             space_threats = self.get_threats_at(row, col)
        #             p1_even_threats += space_threats["1E"]
        #             p2_even_threats += space_threats["2E"]
        #             p1_odd_threats += space_threats["1O"]
        #             p2_odd_threats += space_threats["2O"]
        #     self.threats["1E"] = p1_even_threats
        #     self.threats["1O"] = p1_odd_threats
        #     self.threats["2E"] = p2_even_threats
        #     self.threats["2O"] = p2_odd_threats
        #     print(self.threats)

        # def get_threats_at(self, row, col):
        #     space = self.grid[col][row]
        #     space_threats = {"1E": 0, "1O": 0, "2E": 0, "2O": 0}
        #     if space == Board.BLANK_SPACE:
        #         best_streaks = {Board.PLAYER_ONE: 0, Board.PLAYER_TWO: 0}
        #         current_streak = 0
        #         last_piece = None
        #         for current_col in range(col - 4, col + 5):
        #             # Out of bounds or at space's column, in which case a streak should continue.
        #             if current_col < 0 or current_col == col:
        #                 continue
        #             if current_col > (Board.get_length() - 1):
        #                 if last_piece is not None and last_piece != Board.BLANK_SPACE:
        #                     if current_streak > best_streaks[last_piece]:
        #                         best_streaks[last_piece] = current_streak
        #                 break
        #             current_piece = self.grid[current_col][row]
        #             if current_piece != Board.BLANK_SPACE:
        #                 if last_piece is None:
        #                     current_streak += 1
        #                     last_piece = current_piece
        #                 elif last_piece == current_piece:
        #                     current_streak += 1
        #                 else:
        #                     if last_piece != Board.BLANK_SPACE:
        #                         if current_streak > best_streaks[last_piece]:
        #                             best_streaks[last_piece] = current_streak
        #                             current_streak = 1
        #                     else:
        #                         current_streak = 0
        #                     last_piece = current_piece
        #             else:
        #                 if last_piece is not None and last_piece != Board.BLANK_SPACE:
        #                     if current_streak > best_streaks[last_piece]:
        #                         best_streaks[last_piece] = current_streak
        #                 current_streak = 0
        #                 last_piece = current_piece
        #         even = row % 2 == 0
        #         if even:
        #             if best_streaks[Board.PLAYER_ONE] >= 4:
        #                 space_threats["1E"] = 1
        #             if best_streaks[Board.PLAYER_TWO] >= 4:
        #                 space_threats["2E"] = 1
        #         else:
        #             if best_streaks[Board.PLAYER_ONE] >= 4:
        #                 space_threats["1O"] = 1
        #             if best_streaks[Board.PLAYER_TWO] >= 4:
        #                 space_threats["2O"] = 1
        #
        #     return space_threats
