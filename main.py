import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.border()
    stdscr.addstr(
        curses.LINES // 2,
        curses.COLS // 2 - len("Welcome to wpm.py! Press any key to start.") // 2,
        "Welcome to wpm.py! Press any key to start.",
        ),
    stdscr.refresh()
    stdscr.getkey()
    
def display_text(stdscr, target, current, wpm=0):
    stdscr.border()
    stdscr.addstr(
        curses.LINES // 2,
        curses.COLS // 2 - len(target) // 2,
        target,
        ),
    stdscr.addstr(
        curses.LINES // 2 - 2,
        curses.COLS // 2 - len(str(wpm)) // 2,
        f"WPM: {wpm}"),
    stdscr.refresh()

    for i, char in enumerate (current):

        correct_char = target[i]
        color = curses.color_pair(2)
        if char != correct_char:
            color = curses.color_pair(3)

        stdscr.addstr(curses.LINES // 2, (curses.COLS // 2 - len(target) // 2) + i, char, color)


def wpm_test(stdscr):
    target_text = "hello world lets see how fast you can type this out"
    current_text = []
    wpm = 0
    start_time = time.time()

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round(len(current_text) / 5 / (time_elapsed / 60))

        stdscr.clear()

        display_text(stdscr, target_text, current_text, wpm)

        stdscr.refresh()

        key = stdscr.getkey()

        # Exit on escape button
        if ord(key) == 27:
            break

        if key in("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


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
    # curses.echo()

    stdscr.attron(MAGNETA_AND_BLACK)
    start_screen(stdscr)
    wpm_test(stdscr)
    stdscr.attroff(MAGNETA_AND_BLACK)
    
wrapper(main)

