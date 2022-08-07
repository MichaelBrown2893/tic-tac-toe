import art
from console_app_tools.model_view_presenter import console_view

INSTRUCTIONS = """
Welcome to tic_tac_toe!

Take it in turns to enter the row and column to identify 
the square in which you would like to place an x or an o.

Get three in a row to win!
"""

def app():
    view = console_view.ConsoleView
    print(art.TITLE)
    print(INSTRUCTIONS)

if __name__ == "__main__":
    app()