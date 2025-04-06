# Real-time writing-assistant with Ollama Mistral 7B

This Python project allows you to correct typos, punctuation, and casing of selected or current-line text using a hotkey trigger. It leverages the locally installed [Mistral 7B Instruct model](https://ollama.com/library/mistral:7b-instruct-v0.2-q4_K_S) via [Ollama](https://github.com/ollama/ollama).

## Features

- Fixes grammar, spelling, casing, and punctuation.
- Preserves original line breaks.
- Uses global hotkeys for efficiency:
  - `F9`: Fix **current line**.
  - `F10`: Fix **selected text**.
- Sends selected text to a **locally running** Mistral model via Ollama.
- Automatically pastes the corrected result back in place.

---

## Project Structure
```
writing-assistant/
├── main.py           # The main script to run the assistant
├── README.md         # Documentation of the project
└── requirements.txt  # Python dependencies list

```

---

## Requirements

Make sure you have the following installed on your system:

### Ollama & Mistral 7B Instruct

- Python 3.x
- Required libraries: `pynput`, `pyperclip`, `httpx`. 
- Install Ollama: https://github.com/ollama/ollama
- Install the required model locally:
  
  ```bash
  ollama run mistral:7b-instruct-v0.2-q4_K_S

---

## Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/luanfelixcoding/writing-assistant.git
    cd writing-assistant
    
2. **Create a Virtual Environment (optional, but recommended)**:
    ```bash
    python -m venv .venv

3. **Activate the Virtual Environment (venv)**:
    - On Windows: `.venv/Scripts/activate`
    - On Linux/Mac: `source .venv/bin/activate`

4. **Install Dependencies (if any)**:
    ```bash
    pip install -r requirements.txt

5. **Run the Program**:
    ```bash
    python main.py
    
