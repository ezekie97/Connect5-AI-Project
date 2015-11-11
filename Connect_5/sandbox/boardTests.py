from src.board import *

__author__ = 'Bill'


def all_tests():
    #basic_tests()
    horizontal_victory_tests()
    #vertical_victory_tests()
    #diagonal_victory_tests()


def horizontal_victory_tests():
    print("CHECKING FOR HORIZONTAL VICTORIES")
    b = Board()
    b.drop(1, 1)
    print("Winner? " + str(b.is_winner()))
    b.drop(1, 2)
    b.drop(1, 3)
    b.drop(1, 4)
    b.drop(1, 5)    # Should Result in Win
    print("Winner? " + str(b.is_winner()))
    print(b)

    print("CLEARING BOARD")
    # reset board
    b = Board()
    b.drop(1, 0)
    b.drop(1, 1)
    b.drop(1, 2)
    b.drop(1, 3)
    b.drop(2, 4)    # No Win
    print("Winner? " + str(b.is_winner()))
    print(b)
    print(b.piece_at(0, 6))

    print("CLEARING BOARD")
    # reset board
    b = Board()
    # fill bottom row
    b.drop(1, 0)
    b.drop(2, 1)
    b.drop(1, 2)
    b.drop(2, 3)
    b.drop(1, 4)
    b.drop(2, 5)
    b.drop(1, 6)
    b.drop(1, 0)
    b.drop(1, 1)
    b.drop(1, 3)
    b.drop(1, 4)
    b.drop(1, 2)  # Winner
    print("Winner? " + str(b.is_winner()))
    b.drop(1, 5)  # Winner
    print("Winner? " + str(b.is_winner()))
    b.drop(1, 6)  # Winner
    print("Winner? " + str(b.is_winner()))
    b.drop(1, 7)
    b.drop(1, 7)  # Winner
    print("Winner? " + str(b.is_winner()))
    b.drop(1, 8)
    b.drop(1, 8)  # Winner
    print("Winner? " + str(b.is_winner()))
    print(b)

    print("HORIZONTAL VICTORIES TEST COMPLETE")


def basic_tests():
    print("PERFORMING BASIC TESTS")
    b = Board()
    print("SHOW EMPTY COLUMN")
    print(b.create_empty_column())
    print("SHOW EMPTY BOARD")
    print(b)

    print("FILLING BOARD")
    b.drop(1, 1)
    b.drop(2, 2)
    b.drop(1, 1)
    b.drop(2, 1)
    b.drop(1, 1)
    b.drop(1, 1)
    b.drop(1, 1)
    b.drop(1, 1)
    print("FAILURE MESSAGE SHOULD FOLLOW THIS STATEMENT")
    b.drop(1, 1)  # Fails
    b.drop(1, 0)
    b.drop(1, 2)

    print(b)
    print("BASIC TESTS COMPLETE")


def vertical_victory_tests():
    print("CHECKING FOR VERTICAL VICTORIES")
    b = Board()

    b.drop(1, 1)
    b.drop(1, 1)
    b.drop(1, 1)
    b.drop(1, 1)
    b.drop(1, 1)  # Winner
    print(b)
    print("Winner? " + str(b.is_winner()))
    print("CLEARING BOARD")

    b = Board()

    b.drop(1, 1)
    b.drop(1, 1)
    b.drop(2, 1)
    b.drop(2, 1)
    b.drop(2, 1)
    b.drop(2, 1)
    b.drop(2, 1)  # Winner
    print(b)
    print("Winner? " + str(b.is_winner()))
    print("CLEARING BOARD")

    b = Board()

    b.drop(1, 1)
    b.drop(1, 1)
    b.drop(1, 1)
    b.drop(1, 1)
    b.drop(2, 1)
    b.drop(2, 1)
    b.drop(2, 1)
    print(b)
    print("NO WINNER")
    print("Winner? " + str(b.is_winner()))
    print("VERTICAL VICTORY TESTS COMPLETE")


def diagonal_victory_tests():
    print("BEGINNING DIAGONAL VICTORY TESTS")
    print("UPPER LEFT TO LOWER RIGHT")
    b = Board()
    b.drop(1, 8)
    b.drop(2, 7)
    b.drop(1, 7)
    b.drop(1, 6)
    b.drop(2, 6)
    b.drop(1, 6)
    b.drop(2, 5)
    b.drop(1, 5)
    b.drop(2, 5)
    b.drop(1, 5)
    b.drop(1, 4)
    b.drop(2, 4)
    b.drop(2, 4)
    b.drop(2, 4)
    b.drop(1, 4)  # Winner
    print("Winner? " + str(b.is_winner()))
    print(b)

    print("CLEARING BOARD")

    b = Board()
    b.drop(1, 0)
    b.drop(2, 1)
    b.drop(1, 1)
    b.drop(2, 2)
    b.drop(2, 2)
    b.drop(1, 2)
    b.drop(2, 3)
    b.drop(2, 3)
    b.drop(2, 3)
    b.drop(1, 3)
    b.drop(2, 4)
    b.drop(2, 4)
    b.drop(2, 4)
    b.drop(1, 4)
    b.drop(1, 4)  # Winner
    print(b)
    print("Winner? " + str(b.is_winner()))

    print("DIAGONAL VICTORY TESTS COMPLETE")





all_tests()

