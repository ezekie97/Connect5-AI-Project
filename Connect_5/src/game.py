import pygame
import random
from src.minimax import *

__author__ = 'Bill Ezekiel'


class Game:
    """
    Game for Connect 5. Handles the GUI for the game.
    The game consists of three main components: the mouse area, the board, and the message box.
    The mouse area, when hovered over, will allow players to drop their respective pieces
    into columns, similar to the actual Connect 4 game. The Board is the current game board.
    The message box displays messages about the game, notifying the player when to go, when the
    game has ended, who has won, and several other messages.
    """

    # Initialize pygame components
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()

    # Player Constants
    PLAYER_MOVE_FIRST = "R"  # Red always moves first.
    PLAYER_MOVE_LAST = "B"

    # Image Files
    RED_CHIP = pygame.image.load("../img/red_chip.png")
    BLACK_CHIP = pygame.image.load("../img/black_chip.png")
    BLANK_SPACE = pygame.image.load("../img/blank_space.png")
    RED_SPACE = pygame.image.load("../img/red_space.png")
    BLACK_SPACE = pygame.image.load("../img/black_space.png")
    MOUSE_AREA_BACKGROUND = pygame.image.load("../img/mouse_area_bg.png")
    MSG_BOX = pygame.image.load("../img/msg_box_box.png")
    MSG_BOX_BACKGROUND = pygame.image.load("../img/msg_box_bg.png")
    BOARD_BACKGROUND = pygame.image.load("../img/board_bg.png")
    BOARD_BACKGROUND_OVERLAY = pygame.image.load("../img/board_bg_overlay.png")
    IMG_LENGTH = 50  # All images are squares so this applies to height as well.

    # Sound Effects
    DROP_SOUND = pygame.mixer.Sound("../sfx/drop.wav")
    WIN_SOUND = pygame.mixer.Sound("../sfx/win.wav")
    LOSE_SOUND = pygame.mixer.Sound("../sfx/lose.wav")

    # Message Box Texts
    MSG_WELCOME = "Welcome to Connect 5!"
    MSG_YOUR_TURN = "Your Turn!"
    MSG_AI_TURN = "Waiting for Opponent..."
    MSG_YOU_WIN = "You Win!"
    MSG_AI_WIN = "Computer Wins!"
    MSG_TIE = "Tie!"
    MSG_GAME_OVER = "Game Over."
    MSG_PLAY_AGAIN = "Play again?"
    MSG_INVALID_DROP = "You can't drop a piece there!"

    # Size of window and its components (in pixels).
    # Window Dimensions = 450px x 540px
    BOARD_LENGTH = Board.get_length() * IMG_LENGTH
    BOARD_HEIGHT = Board.get_height() * IMG_LENGTH
    MOUSE_AREA_LENGTH = Board.get_length()
    MOUSE_AREA_HEIGHT = 90
    MSG_BOX_LENGTH = Board.get_length() * IMG_LENGTH
    MSG_BOX_HEIGHT = 100
    WINDOW_LENGTH = Board.get_length() * IMG_LENGTH
    WINDOW_HEIGHT = BOARD_HEIGHT + MOUSE_AREA_HEIGHT + MSG_BOX_HEIGHT
    PADDING = 20

    def __init__(self):
        """
        Generate a game object and start the game.
        """
        self.board = Board()
        self.game_over = False
        self.player_one = None  # Human is player one.
        self.player_two = None  # AI is player two.
        self.control = 0
        # Randomly Choose order of play
        self.decide_first_player()
        self.minimax = MiniMax(self.player_one, self.player_two)
        self.window = self.init_window()
        pygame.display.flip()
        self.begin()

    def init_window(self):
        """
        Generate an initialize pygame window of the 'Connect_5' game.
        :return: a pygame window with the game initialized
        """
        size = self.WINDOW_LENGTH, self.WINDOW_HEIGHT
        screen = pygame.display.set_mode(size)
        caption = "Connect 5"
        pygame.display.set_caption(caption)

        # Initialize Mouse Area
        self.clear_mouse_area(screen)

        # Initialize Board Area
        self.draw_board(screen)

        # Initialize Message Box Area with preliminary text.
        if self.control == self.player_one:  # player_one is human
            self.refresh_msg_box(screen, self.MSG_YOUR_TURN)
        else:  # player_two is not.
            self.refresh_msg_box(screen, self.MSG_AI_TURN)
        return screen

    def clear_mouse_area(self, screen):
        """
        Clear the mouse area of everything but the background picture.
        :param screen: The game screen
        """
        position = 0, 0
        screen.blit(self.MOUSE_AREA_BACKGROUND, position)

    def decide_first_player(self):
        """
        Randomly Choose which player goes first and set control of the board to
        that player.
        """
        player = random.randint(1, 2)
        if player == 2:
            self.player_one = self.PLAYER_MOVE_LAST
            self.player_two = self.PLAYER_MOVE_FIRST
        else:
            self.player_one = self.PLAYER_MOVE_FIRST
            self.player_two = self.PLAYER_MOVE_LAST
        self.control = self.PLAYER_MOVE_FIRST

    def switch_players(self):
        """
        Switch which player's turn it is.
        """
        if self.control == self.PLAYER_MOVE_FIRST:
            self.control = self.PLAYER_MOVE_LAST
        else:
            self.control = self.PLAYER_MOVE_FIRST

    def draw_board(self, screen):
        """
        Draw the current Connect 5 Board on the given screen.
        :param screen: The screen
        """
        bg_position = 0, self.MOUSE_AREA_HEIGHT
        screen.blit(self.BOARD_BACKGROUND, bg_position)
        screen.blit(self.BOARD_BACKGROUND_OVERLAY, bg_position)
        for i in range(0, self.board.get_height()):
            for j in range(0, self.board.get_length()):
                screen_position = j * self.IMG_LENGTH, (i * self.IMG_LENGTH) + self.MOUSE_AREA_HEIGHT
                player = self.board.piece_at(i, j)
                if player == self.PLAYER_MOVE_FIRST:
                    screen.blit(self.RED_SPACE, screen_position)
                elif player == self.PLAYER_MOVE_LAST:
                    screen.blit(self.BLACK_SPACE, screen_position)
                else:
                    screen.blit(self.BLANK_SPACE, screen_position)

    def refresh_msg_box(self, screen, text):
        """
        Refresh the message box with next text
        :param screen: the game window
        :param text: the new text to display.
        """
        position = 0, (self.MOUSE_AREA_HEIGHT + self.BOARD_HEIGHT)
        screen.blit(self.MSG_BOX_BACKGROUND, position)
        screen.blit(self.MSG_BOX, position)
        font = pygame.font.Font(None, 36)
        msg_text = font.render(text, 1, (0, 0, 0))
        position = 20, (self.MOUSE_AREA_HEIGHT + self.BOARD_HEIGHT + self.PADDING)
        screen.blit(msg_text, position)

    def mouse_move_event(self, event, screen):
        """
        Handles actions dealing with MOUSEMOTION event types.
        :param event: the MOUSEMOTION event
        :param screen: the game window.
        """
        position = 0, 0
        screen.blit(self.MOUSE_AREA_BACKGROUND, position)
        mouse_position = event.pos
        if self.control == self.player_one:  # show the player
            if self.in_mouse_area(mouse_position):
                x = mouse_position[0]
                col = x // self.IMG_LENGTH
                position = (50 * col, 30)
                if self.control == self.PLAYER_MOVE_FIRST:
                    # Red's Move
                    screen.blit(self.RED_CHIP, position)
                else:
                    # Black's Move
                    screen.blit(self.BLACK_CHIP, position)

    def mouse_click_event(self, event, screen):
        """
        Handles actions dealing with MOUSEBUTTONUP event types.
        :param event: the MOUSEBUTTONUP event
        :param screen: the game window.
        """
        mouse_position = event.pos
        if self.in_mouse_area(mouse_position):
            x = mouse_position[0]
            col = x // self.IMG_LENGTH
            if self.board.can_drop(col)[0]:
                self.board.drop(self.control, col)
                self.draw_board(screen)
                self.DROP_SOUND.play()
                winner = self.board.find_winner()
                if winner == self.player_one:  # Winner Human Player
                    self.refresh_msg_box(screen, self.MSG_GAME_OVER + " " + self.MSG_YOU_WIN)
                    self.WIN_SOUND.play()
                    self.game_over = True
                    self.clear_mouse_area(screen)
                elif self.board.is_filled():  # Tie, board is filled with no winner.
                    self.refresh_msg_box(screen, self.MSG_TIE + " " + self.MSG_GAME_OVER)
                    self.LOSE_SOUND.play()
                    self.game_over = True
                    self.clear_mouse_area(screen)
                else:  # Game continues
                    self.switch_players()
                    # Refresh Mouse Area with Correct Players Piece.
                    self.mouse_move_event(event, screen)
                    self.refresh_msg_box(screen, self.MSG_AI_TURN)
                    pygame.display.flip()
                    self.ai_take_turn(self.window)
            else:
                self.refresh_msg_box(screen, self.MSG_INVALID_DROP)

    def in_mouse_area(self, pos):
        """
        Check if the mouse cursor is in the MOUSE_AREA
        :param pos: the position of the mouse cursor
        :return: True if the cursor is in the MOUSE_AREA
        """
        y = pos[1]
        # Since the the length of the mouse area is the length of the window,
        # the x value doesn't matter.
        return 0 < y <= self.MOUSE_AREA_HEIGHT

    def ai_take_turn(self, screen):
        """
        AI makes its move.
        :param screen: the game screen
        """
        node = BoardNode(self.board, MiniMax.NEG_INF)
        best_board = self.minimax.mini_max(node, MiniMax.NEG_INF, MiniMax.INF, 3).get_board()
        col = best_board.get_last_move()[1]
        self.board.drop(self.player_two, col)
        winner = self.board.find_winner()
        self.draw_board(screen)
        self.DROP_SOUND.play()
        if winner == self.player_two:  # AI player
            self.refresh_msg_box(screen, self.MSG_GAME_OVER + " " + self.MSG_AI_WIN)
            self.LOSE_SOUND.play()
            self.game_over = True
            self.clear_mouse_area(screen)
        elif self.board.is_filled():  # Tie, board is filled with no winner.
            self.refresh_msg_box(screen, self.MSG_TIE + " " + self.MSG_GAME_OVER)
            self.LOSE_SOUND.play()
            self.game_over = True
            self.clear_mouse_area(screen)
        else:
            self.switch_players()
            self.refresh_msg_box(screen, self.MSG_YOUR_TURN)
        self.minimax.heuristic_finder.heuristic(self.board)

    def begin(self):
        """
        Begin the game, as of right now it is not playable however holding and releasing keys
        changes the text in the message box.
        """
        window_open = True
        while window_open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    window_open = False
                if self.control == self.player_one:  # Human's turn
                    if not self.game_over:
                        if event.type == pygame.MOUSEMOTION:
                            self.mouse_move_event(event, self.window)
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.mouse_click_event(event, self.window)
                else:
                    if not self.game_over:  # if AI goes first.
                        self.ai_take_turn(self.window)
            pygame.display.flip()


# Create a game, which starts it.
g = Game()
