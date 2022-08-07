import art

INSTRUCTIONS = """
Welcome to tic-tac-toe!

Take it in turns to enter the row and column to identify 
the square in which you would like to place an x or an o.

Get three in a row to win!
"""

def app():
    print(art.TITLE)
    print(INSTRUCTIONS)

if __name__ == "__main__":
    app()