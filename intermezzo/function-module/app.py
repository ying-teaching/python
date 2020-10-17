
import turtle

SCREEN_WIDTH = 600    # Screen width
SCREEN_HEIGHT = 600   # Screen height

# v1
# from hit_target_game import *

# v2
from hit_target_game import run_game

# v3, need to put the module as prefix
# import hit_target_game 

def setup_window():
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    pen = turtle.Pen()
    return pen


# Hit the Target Game
def main():
    pen = setup_window()
    run_game(pen)
    turtle.done()

if __name__ == '__main__':
    main()
