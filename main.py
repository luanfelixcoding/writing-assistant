from pynput import keyboard
from pynput.keyboard import Key, Controller


def fix_current_line():
    ...


def fix_selection():
    ...


def on_f9():
    fix_current_line()


def on_f10():
    fix_selection()


# print(Key.f9.value, Key.f10.value)
# OUTPUT: <120> <121>

with keyboard.GlobalHotKeys({
    '<120>': on_f9,
    '<121>': on_f10,
}) as h:
    h.join()
