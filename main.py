import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    RED_AND_BLACK = curses.color_pair(1)
    YELLOW_AND_BLACK = curses.color_pair(2)

    counter_window = curses.newwin(1, 20, 10, 10)
    stdscr.addstr("Hello World!")
    stdscr.refresh()

    for i in range(100):
        counter_window.clear()
        color = RED_AND_BLACK if i % 2 == 0 else YELLOW_AND_BLACK
        counter_window.addstr(f"Count: {i}", color)
        counter_window.refresh()
        time.sleep(0.1)
    stdscr.getkey()

wrapper(main)