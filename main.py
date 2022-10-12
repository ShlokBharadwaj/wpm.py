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

    win = curses.newwin(3, 18, 2, 2)
    box = Textbox(win)
    
    rectangle(stdscr, 2, 2, 5, 20)
    stdscr.refresh()

    box.edit()

    stdscr.getch()

wrapper(main)