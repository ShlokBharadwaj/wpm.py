import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    WHITE_AND_BLACK = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_BLACK = curses.color_pair(3)
    YELLOW_AND_BLACK = curses.color_pair(4)
    stdscr.nodelay(True)
    
    x, y = 0, 0
    string_x = 0
    while True: 
        try:
            key = stdscr.getkey()
        except:
            key = None
        if key == 'KEY_UP': 
            y -= 1
        elif key == 'KEY_DOWN':
            y += 1
        elif key == 'KEY_LEFT':
            x -= 1
        elif key == 'KEY_RIGHT':
            x += 1

        stdscr.clear()
        string_x += 1
        stdscr.addstr(0, string_x//100, "Hello World!")

        stdscr.addstr(y, x, "0")
        stdscr.refresh()


wrapper(main)