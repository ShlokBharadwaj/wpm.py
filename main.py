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
    
def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

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
        f"WPM: {wpm}", curses.color_pair(1)),

    for i, char in enumerate (current):

        correct_char = target[i]
        color = curses.color_pair(2)
        if char != correct_char:
            color = curses.color_pair(3)

        stdscr.addstr(curses.LINES // 2, (curses.COLS // 2 - len(target) // 2) + i, char, color)


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
 
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round(len(current_text) / 5 / (time_elapsed / 60))

        stdscr.erase()
        # stdscr.idcok(False)
        # stdscr.idlok(False)
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh() 

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

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
    curses.init_pair(9, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.echo()

    stdscr.attron(curses.color_pair(4))
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(curses.LINES // 2 + 2, curses.COLS // 2 - len("You have completed the text! Press escape key to exit.") // 2, "You have completed the text! Press escape key to exit.", curses.color_pair(5))
        key = stdscr.getkey()
        if ord(key) == 27:
            break
    stdscr.attroff(curses.color_pair(4))
    
wrapper(main)

