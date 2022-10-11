import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    # stdscr.addstr(1, 1, "Hello World!", curses.A_ALTCHARSET)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_BLINK)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_BOLD)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_DIM)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_INVIS)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_ITALIC)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_NORMAL)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_PROTECT)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_REVERSE)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_STANDOUT)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_UNDERLINE)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_HORIZONTAL)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_LEFT)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_LOW)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_RIGHT)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_TOP)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_VERTICAL)
    # stdscr.addstr(1, 1, "Hello World!", curses.A_CHARTEXT)
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)