import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_GREEN, curses.COLOR_YELLOW)
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_WHITE)
    WHITE_AND_BLACK = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_BLACK = curses.color_pair(3)
    MAGNETA_AND_BLACK = curses.color_pair(4)
    CYAN_AND_BLACK = curses.color_pair(5)
    BLUE_AND_BLACK = curses.color_pair(6)
    GREEN_AND_YELLOW = curses.color_pair(7)
    BLACK_AND_WHITE = curses.color_pair(8)
    curses.echo()

    stdscr.attron(MAGNETA_AND_BLACK)
    stdscr.border()
    stdscr.attroff(MAGNETA_AND_BLACK)
    
    stdscr.refresh()
    stdscr.getkey()
wrapper(main)