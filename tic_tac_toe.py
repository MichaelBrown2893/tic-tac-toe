import sys
from dataclasses import dataclass
from typeguard import typechecked
from console_app_tools.model_view_presenter import ConsolePresenter, ConsoleModel
from console_app_tools.user_input import get_input_of_type, get_input
from observer_pattern.observer_pattern import Subject, Observer


class GameBoard(Subject):
    GAME_SYMBOLS: str = ["O", "X"]

    _BLANK_GAME_BOARD: list[list[str]] = [["1", "2", "3"],
                                          ["4", "5", "6"],
                                          ['7', "8", "9"]]

    _HORIZONTAL_LINE: str = "-----------"

    _game_board: list[list[str]] = _BLANK_GAME_BOARD
    _observers: list = []

    def __init__(self):
        self._observers = []
        self._game_board = self._BLANK_GAME_BOARD

    def __str__(self) -> str:
        return "\n".join([f" {self._game_board[0][0]} | {self._game_board[0][1]} | {self._game_board[0][2]}",
                          self._HORIZONTAL_LINE,
                          f" {self._game_board[1][0]} | {self._game_board[1][1]} | {self._game_board[1][2]}",
                          self._HORIZONTAL_LINE,
                          f" {self._game_board[2][0]} | {self._game_board[2][1]} | {self._game_board[2][2]}"])

    @typechecked
    def attach(self, observer: Observer) -> None:
        """Attaches an observer to this subject

        Parameters
        ----------
        observer
            Class that will observe the change to the state of this subject

        Raises
        ------
        TypeError
            Type for observer argument was not of type Observer
        """
        self._observers.append(observer)

    @typechecked
    def detach(self, observer) -> None:
        """Removes an observer from this subject

        Parameters
        ----------
        observer
            Class that is observing the change to the state of this subject

        Raises
        ------
        TypeError
            Type for observer argument was not of type Observer
        """
        self._observers.remove(observer)

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """
        for observer in self._observers:
            observer.update(self)

    @staticmethod
    def _cell_number_to_2d(cell_number: int) -> (int, int):
        return (cell_number-1) // 3, ((cell_number-1) % 3)

    def place_symbol(self, cell: int, symbol: str) -> None:
        if symbol.upper() not in self.GAME_SYMBOLS:
            raise ValueError(
                f"Symbol {symbol} is not valid for tic-tac-toe. Use one of the following: {self.GAME_SYMBOLS}")
        if not (1 <= cell <= 9):
            raise ValueError(
                f"Number {cell} is not a valid cell. Enter a number between 1 - 9."
            )
        cell_coords = self._cell_number_to_2d(cell)
        if not self._game_board[cell_coords[0]][cell_coords[1]].isnumeric():
            raise ValueError(
                f"Cell {cell} has already been chosen, choose another cell."
            )
        self._game_board[cell_coords[0]][cell_coords[1]] = symbol
        self.notify()

    def _check_rows(self) -> bool:
        for row in self._game_board:
            if len(set(row)) == 1:
                return True

        return False

    def _check_col(self, col_number: int) -> bool:
        return len({
            self._game_board[0][col_number],
            self._game_board[1][col_number],
            self._game_board[2][col_number]
        }) == 1

    def _check_cols(self) -> bool:
        for col in range(3):
            if self._check_col(col):
                return True

        return False

    def _check_diagonals(self) -> bool:
        if len(set(
            [self._game_board[i][i] for i in range(3)]
        )) == 1:
            return True

        if len(set(
            [self._game_board[i][2 - i] for i in range(3)]
        )) == 1:
            return True

        return False

    def game_over(self) -> bool:
        return self._check_diagonals() or self._check_cols() or self._check_rows()


class GameConsoleModel(ConsoleModel, Observer):
    TITLE = """
 _____  _                _____                       _____            
|_   _|(_)              |_   _|                     |_   _|             
  | |   _   ___  ______   | |    __ _   ___  ______   | |    ___    ___ 
  | |  | | / __||______|  | |   / _` | / __||______|  | |   / _ \  / _ \\
  | |  | || (__           | |  | (_| || (__           | |  | (_) ||  __/
  \_/  |_| \___|          \_/   \__,_| \___|          \_/   \___/  \___|
"""

    INSTRUCTIONS: str = """
Welcome to tic_tac_toe!

Take it in turns to enter the row and column to identify 
the square in which you would like to place an 'x' or an 'o'.

Get three in a row to win!
"""

    def __init__(self, presenter: ConsolePresenter = ConsolePresenter()):
        super(GameConsoleModel, self).__init__(observer=presenter)

    def update(self, subject: Subject) -> None:
        self.clear_content()
        self.add_lines([
            self.TITLE,
            self.INSTRUCTIONS,
            subject.__str__()
        ])
        self.notify()

    def welcome(self) -> None:
        self.clear_content()
        self.add_lines([
            self.TITLE,
            self.INSTRUCTIONS
        ])
        self.notify()


@dataclass
class Player:
    player_number: int
    symbol: str

    def __init__(self, player_number: int, symbol: str):
        self.player_number = player_number
        self.symbol = symbol


class TurnTracker:
    players_turn: int = 1

    def next_turn(self):
        self.players_turn += 1
        if self.players_turn > 2:
            self.players_turn -= 2


class TicTacToe:
    _board: GameBoard
    _model: GameConsoleModel
    _players: list[Player] = []

    def __init__(self) -> None:
        self._board = GameBoard()
        self._model = GameConsoleModel()
        self._board.attach(self._model)
        self._model.update(self._board)
        self._players.append(Player(1, self._board.GAME_SYMBOLS[0]))
        self._players.append(Player(2, self._board.GAME_SYMBOLS[1]))

    @staticmethod
    def _input_prompt(player: Player) -> str:
        return f"Player {player.player_number} please enter the cell you'd like to place a {player.symbol} in: "

    def _take_turn(self, player: Player) -> None:
        try:
            self._board.place_symbol(get_input_of_type(int, self._input_prompt(player)), player.symbol)
        except ValueError as err:
            print(err)
            self._take_turn(player)

    def _game_over(self, winner: Player):
        print(f"Player {winner.player_number} won with 3 in a row!")

    def play_game(self):
        turn_tracker = TurnTracker()

        while True:
            self._take_turn(self._players[turn_tracker.players_turn - 1])
            if self._board.game_over():
                break
            turn_tracker.next_turn()

        self._game_over(self._players[turn_tracker.players_turn -1])