from tic_tac_toe import *
from console_app_tools.Input import user_input


def tic_tac_toe():
    TicTacToe().play_game()


def play_again() -> bool:
    return user_input.get_yes_or_no("Would you like to play again 'y' or 'n'?: ")


if __name__ == "__main__":
    tic_tac_toe()
    while play_again():
        tic_tac_toe()
