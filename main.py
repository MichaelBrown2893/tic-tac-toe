from tic_tac_toe import *
from console_app_tools import user_input

def tic_tac_toe():
    game = GameModel()

    game.place_symbol(user_input.get_input_of_type(input_type=int, prompt="Enter a number: "), "x")


if __name__ == "__main__":
    tic_tac_toe()
