__author__ = 'Bill'


class Board:
    """
    Class for the Connect 5 Game Board. The Board is always a 7 long by
    9 high. A board always remembers the last move made.
    """

    # Class Constants
    BLANK_SPACE = "_"  # Blank Space
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
        Get the value of the piece at the specified location.
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
        Drop a piece into a column.
        :param dropped_char: the value of the piece being dropped.
        :param col_num: the column to drop the piece into.
        :return: true if the drop was successful or false if the column is full.
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
        :param piece: the value of the piece.
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
        :param piece: the value of the piece
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
        :param piece: the value of the piece
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
        :param piece: the value of the piece
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
                break
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
                break
            else:
                streak += 1
        if streak == n:
            result += 1

        return result

    def find_winner(self):
        """
        Check if the current board has a winner. A winner has 5 in a row horizontally, vertically, or diagonally.
        :return: a character representing a player, or None if there is no winner.
        """
        win_amount = self.SCORE_TO_WIN
        if self.find_n_in_a_row(Board.PLAYER_ONE, win_amount) >= 1:
            return Board.PLAYER_ONE
        elif self.find_n_in_a_row(Board.PLAYER_TWO, win_amount) >= 1:
            return Board.PLAYER_TWO
        else:
            return None

    def find_disconnected_wins(self, piece):
        """
        Find blank areas that, when filled in with the given type of piece, cause a victory
        for that piece.
        :param piece: the player piece
        :return: the number of unconnected wins.
        """
        count = 0
        for row in range(0, Board.get_height()):
            for col in range(0, Board.get_length()):
                current_piece = self.grid[col][row]
                if current_piece == Board.BLANK_SPACE:
                    count += self.find_horizontal_disconnected_wins(piece, col, row)
                    count += self.find_disconnected_diagonal_wins(piece, col, row)
        return count

    def find_horizontal_disconnected_wins(self, piece, col_num, row_num):
        """
        :param piece: the character to check for.
        :param col_num: the column number of the last move made.
        :param row_num: the row number of the last move made.
        :return: 1 if the filled in blank piece causes a horizontal victory for its corresponding player.
        """
        connection = 1
        curr_col = col_num - 1
        while curr_col >= 0:
            if self.grid[curr_col][row_num] == piece:
                connection += 1
                curr_col -= 1
            else:  # can't possibly have a longer connection this way.
                break

        curr_col = col_num + 1
        while curr_col < self.BOARD_LENGTH:
            if self.grid[curr_col][row_num] == piece:
                connection += 1
                curr_col += 1
            else:  # can't possibly have a longer connection this way.
                break
        if connection >= 4:
            return 1
        return 0

    def find_disconnected_diagonal_wins(self, piece, col_num, row_num):
        """
        :param piece: the character to check for.
        :param col_num: the column number of the last move made.
        :param row_num: the row number of the last move made.
        :return: 1 if the filled in blank piece causes a diagonal victory for its corresponding player.
        """
        result = 0
        connection = 1
        # Upper Left to Lower Right Diagonal
        curr_row = row_num - 1
        curr_col = col_num - 1
        while curr_row >= 0 and curr_col >= 0:
            if self.grid[curr_col][curr_row] == piece:
                connection += 1
                curr_col -= 1
                curr_row -= 1
            else:  # can't possibly have a longer connection this way.
                break

        curr_row = row_num + 1
        curr_col = col_num + 1

        while curr_row < self.BOARD_HEIGHT and curr_col < self.BOARD_LENGTH:
            if self.grid[curr_col][curr_row] == piece:
                connection += 1
                curr_col += 1
                curr_row += 1
            else:  # can't possibly have a longer connection this way.
                break

        if connection >= 4:
            result += 1

        # Lower Left to Upper Right Diagonal
        connection = 1
        curr_row = row_num - 1
        curr_col = col_num + 1
        while curr_row >= 0 and curr_col < self.BOARD_LENGTH:
            if self.grid[curr_col][curr_row] == piece:
                connection += 1
                curr_row -= 1
                curr_col += 1
            else:  # can't possibly have a longer connection this way.
                break

        curr_row = row_num + 1
        curr_col = col_num - 1
        while curr_row < self.BOARD_HEIGHT and curr_col >= 0:
            if self.grid[curr_col][curr_row] == piece:
                connection += 1
                curr_row += 1
                curr_col -= 1
            else:  # can't possibly have a longer connection this way.
                break
        if connection >= 4:
            result += 1
        return result

    def create_grid(self):
        """
        :return: a 2-dimensional array representing the game grid.
        """
        grid = []
        for i in range(0, self.BOARD_LENGTH):
            grid.append(self.create_empty_column())
        return grid

    def get_last_move(self):
        """
        :return: An array containing information about the last move, including the value
         of the piece, the column, and the row.
        """
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
