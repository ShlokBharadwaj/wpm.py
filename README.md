# wpm.py
Simple cli typing game written in Python.

[wpm.webm](https://user-images.githubusercontent.com/79036875/195963242-7ee9fcf2-103a-4a4f-9193-9c9796bdd853.webm)

# About

_wpm.py_ is minimalistic typing test based on user provided exercising text. It is written in Python and uses the [curses](https://docs.python.org/3/howto/curses.html) library for the UI.

# Installation

_wpm.py_ can be downloaded from the Github Repo:
    
    git clone git@github.com:ShlokBharadwaj/wpm.py.git

_wpm.py_ uses curses module which is a part of the standard library. However, it is not available on Windows. If you are on Windows, you can install it using pip:

    pip install windows-curses

# Usage

_wpm.py_ can be run by executing the following command:

    python3 wpm.py

I personally use alias:

```
alias wpm='python3 ~/path/to/wpm.py'
```
because I am too lazy to type python3 everytime.

# When backspace behaves weirdly

Every terminal emulator is different and some of them have weird backspace behaviour( They send different values for key presses of `backspace`, `ctrl+backspace` and `alt+backspace` ). If you are using a terminal emulator that has this problem, you can try to fix it by changing the `BACKSPACE` variable in the `wpm.py` file. The default value is `127` which is the value for `backspace` in most terminal emulators. You can find the value for your terminal emulator by running the following command:

    python3 -c "import curses; print(curses.KEY_BACKSPACE)"

If pressing backspace throws error, then try `ctrl+backspace` and `alt+backspace` and use the value that works.
