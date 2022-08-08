import art
from console_app_tools.model_view_presenter import *

INSTRUCTIONS = """
Welcome to tic_tac_toe!

Take it in turns to enter the row and column to identify 
the square in which you would like to place an x or an o.

Get three in a row to win!
"""

def app():
    model = ConsoleModel()
    presenter = ConsolePresenter(model)
    model.add_line(art.TITLE)
    model.add_line(INSTRUCTIONS)

if __name__ == "__main__":
    app()