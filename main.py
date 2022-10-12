import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    RED_AND_BLACK = curses.color_pair(1)
    YELLOW_AND_BLACK = curses.color_pair(2)

    pad = curses.newpad(100, 100)
    # curses.LINES - 1, curses.COLS - 1 
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67 + j)
            pad.addstr(char, YELLOW_AND_BLACK)

    for i in range(100):
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(i, 0, 0, 0, 20, 20)
        time.sleep(0.1)
    stdscr.getkey()

wrapper(main)