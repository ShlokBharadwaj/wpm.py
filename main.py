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


    stdscr.attron(RED_AND_BLACK)
    stdscr.border()
    stdscr.attroff(RED_AND_BLACK)

    stdscr.attron(GREEN_AND_BLACK)
    rectangle(stdscr, 1, 1, 10, 10)
    stdscr.addstr(5, 30, "Hello World!")
    stdscr.attroff(GREEN_AND_BLACK)

    
    stdscr.move(30, 10)
    
    stdscr.refresh()

    stdscr.getch()

wrapper(main)