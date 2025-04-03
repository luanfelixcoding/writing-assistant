# Keyboard Hotkeys Handler  

This Python script listens for specific function key presses (F9 and F10) and triggers corresponding actions.  

## Features  
- Press **F9** to execute `fix_current_line()` (currently not implemented).  
- Press **F10** to execute `fix_selection()` (currently not implemented).  
- Uses `pynput` to listen for keyboard input globally.  

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/luanfelixcoding/writing-assistant.git
   cd writing-assistant
   ```

2. **Create and Activate a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   venv/Scripts/activate   # On Linux/Mac: source venv/bin/activate
   ```

## Requirements  
Make sure you have `pynput` installed:  
```sh
pip install pynput
