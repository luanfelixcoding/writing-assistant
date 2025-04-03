from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import time

controller = Controller()


def fix_text(text: str) -> str:
    return text[::-1]


def fix_current_line():
    ...


def fix_selection():
    # 1. copy from clipboard
    with controller.pressed(Key.ctrl):
        controller.tap('c')

    # 2. get the text from clipboard
    time.sleep(0.1)
    text = pyperclip.paste()

    # 3. fix text
    fixed_text = fix_text(text)

    # 4. copy back to clipboard
    pyperclip.copy(fixed_text)
    time.sleep(0.1)

    # 5. insert/show text
    with controller.pressed(Key.ctrl):
        controller.tap('v')


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
