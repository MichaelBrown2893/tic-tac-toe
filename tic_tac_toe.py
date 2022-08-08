from dataclasses import dataclass

import art
from console_app_tools.model_view_presenter import ConsolePresenter, ConsoleModel


class GameModel(ConsoleModel):
    INSTRUCTIONS = """
Welcome to tic_tac_toe!

Take it in turns to enter the row and column to identify 
the square in which you would like to place an 'x' or an 'o'.

Get three in a row to win!
"""

    BLANK_GAME_BOARD = ["1", "2", "3",
                        "4", "5", "6",
                        "7", "8", "9"]

    CIRCLE_SYMBOL = "O"
    CROSS_SYMBOL = "X"
    GAME_SYMBOLS = [CIRCLE_SYMBOL, CROSS_SYMBOL]

    HORIZONTAL_LINE = "-----------"

    game_board = BLANK_GAME_BOARD

    def __init__(self, presenter: ConsolePresenter = ConsolePresenter()):
        super(GameModel, self).__init__(observer=presenter)

    def generate_game_board(self) -> str:
        rows = [f" {self.game_board[0]} | {self.game_board[1]} | {self.game_board[2]}",
                self.HORIZONTAL_LINE,
                f" {self.game_board[3]} | {self.game_board[4]} | {self.game_board[5]}",
                self.HORIZONTAL_LINE,
                f" {self.game_board[6]} | {self.game_board[7]} | {self.game_board[8]}"]
        return "\n".join(rows)

    def place_symbol(self, cell: int, symbol: str) -> None:
        if symbol.upper() not in self.GAME_SYMBOLS:
            raise ValueError(
                f"Symbol {symbol} is not valid for tic-tac-toe. Use one of the following: {self.GAME_SYMBOLS}")
        self.game_board[cell] = symbol
        self._update_content()

    def _update_content(self):
        self.clear_content()
        self.add_lines([
            art.TITLE,
            self.INSTRUCTIONS,
            self.generate_game_board()
        ])
        self.notify()


@dataclass
class Player:
    player_number: int
    symbol: str


