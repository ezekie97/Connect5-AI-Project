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

    def drop(self, dropped_char, col_num):
        """
        Drop a piece into a column. If a piece cannot be dropped in a column, the player will
        be notified.
        :param dropped_char: the character of the player dropping the piece
        :param col_num: the column to drop a piece into.
        :return: true if the drop was successful.
        """
        blank_found = False
        row_num = self.BOARD_HEIGHT - 1
        while not blank_found and row_num >= 0:
            if self.grid[col_num][row_num] is not self.BLANK_SPACE:
                row_num -= 1
            else:
                blank_found = True
        if blank_found:
            self.grid[col_num][row_num] = dropped_char
            self.last_move = [dropped_char, col_num, row_num]
            return True
        else:
            return False

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

    def is_winner(self):
        """
        Check if the latest move created a victory.
        :return: true if the player won (has a diagonal, vertical, or horizontal
        line of length 5 or more.
        """
        if self.last_move is None:
            return False
        dropped_char = self.last_move[0]
        col_num = self.last_move[1]
        row_num = self.last_move[2]
        return (self.has_horizontal_win(dropped_char, col_num, row_num) or
                self.has_vertical_win(dropped_char, col_num, row_num) or
                self.has_diagonal_win(dropped_char, col_num, row_num))

    def has_horizontal_win(self, dropped_char, col_num, row_num):
        """
        :param dropped_char: the character to check for.
        :param col_num: the column number of the last move made.
        :param row_num: the row number of the last move made.
        :return: true if the player won (has a horizontal line of length 5 or more)
        """
        connection = 1
        curr_col = col_num - 1
        while curr_col >= 0:
            if self.grid[curr_col][row_num] == dropped_char:
                connection += 1
                curr_col -= 1
            else:  # can't possibly have a longer connection this way.
                break

        curr_col = col_num + 1
        while curr_col < self.BOARD_LENGTH:
            if self.grid[curr_col][row_num] == dropped_char:
                connection += 1
                curr_col += 1
            else:  # can't possibly have a longer connection this way.
                break
        return connection >= self.SCORE_TO_WIN

    def has_vertical_win(self, dropped_char, col_num, row_num):
        """
        :param dropped_char: the character to check for.
        :param col_num: the column number of the last move made.
        :param row_num: the row number of the last move made.
        :return: true if the player won (has a vertical line of length 5 or more)
        """
        connection = 1
        curr_row = row_num - 1
        while curr_row >= 0:
            if self.grid[col_num][curr_row] == dropped_char:
                connection += 1
                curr_row -= 1
            else:  # can't possibly have a longer connection this way.
                break
        curr_row = row_num + 1
        while curr_row < self.BOARD_HEIGHT:
            if self.grid[col_num][curr_row] == dropped_char:
                connection += 1
                curr_row += 1
            else:  # can't possibly have a longer connection this way.
                break
        return connection >= self.SCORE_TO_WIN

    def has_diagonal_win(self, dropped_char, col_num, row_num):
        """
        :param dropped_char: the character to check for.
        :param col_num: the column number of the last move made.
        :param row_num: the row number of the last move made.
        :return: true if the player won (has a diagonal line of length 5 or more)
        """
        connection = 1

        # Upper Left to Lower Right Diagonal
        curr_row = row_num - 1
        curr_col = col_num - 1
        while curr_row >= 0 and curr_col >= 0:
            if self.grid[curr_col][curr_row] == dropped_char:
                connection += 1
                curr_col -= 1
                curr_row -= 1
            else:  # can't possibly have a longer connection this way.
                break

        curr_row = row_num + 1
        curr_col = col_num + 1

        while curr_row < self.BOARD_HEIGHT and curr_col < self.BOARD_LENGTH:
            if self.grid[curr_col][curr_row] == dropped_char:
                connection += 1
                curr_col += 1
                curr_row += 1
            else:  # can't possibly have a longer connection this way.
                break

        if connection >= self.SCORE_TO_WIN:
            return True

        # Lower Left to Upper Right Diagonal
        connection = 1
        curr_row = row_num - 1
        curr_col = col_num + 1
        while curr_row >= 0 and curr_col < self.BOARD_LENGTH:
            if self.grid[curr_col][curr_row] == dropped_char:
                connection += 1
                curr_row -= 1
                curr_col += 1
            else:  # can't possibly have a longer connection this way.
                break

        curr_row = row_num + 1
        curr_col = col_num - 1
        while curr_row < self.BOARD_HEIGHT and curr_col >= 0:
            if self.grid[curr_col][curr_row] == dropped_char:
                connection += 1
                curr_row += 1
                curr_col -= 1
            else:  # can't possibly have a longer connection this way.
                break
        return connection >= self.SCORE_TO_WIN

    def create_grid(self):
        """
        :return: the game grid.
        """
        grid = []
        for i in range(0, self.BOARD_LENGTH):
            grid.append(self.create_empty_column())
        return grid

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
