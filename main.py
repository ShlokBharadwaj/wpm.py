import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.Color.RED, curses.Color.BLACK)
    curses.init_pair(2, curses.Color.YELLOW, curses.Color.BLACK)
    RED_AND_BLACK = curses.color_pair(1)
    YELLOW_AND_BLACK = curses.color_pair(2)


    stdscr.clear()
    stdscr.addstr(0, 0, "Hello World!", RED_AND_BLACK)
    stdscr.addstr(10, 10, "Hello World!", YELLOW_AND_BLACK)
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)