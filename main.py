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

    
    key = stdscr.getkey()
    stdscr.addstr(10, 10, f"Key pressed: {key}")
    stdscr.refresh()
    stdscr.getch()


wrapper(main)