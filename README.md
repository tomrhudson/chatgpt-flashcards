# chatgpt-flashcards

A CLI tool that generates [Anki](https://apps.ankiweb.net/) flashcards from clipboard text using OpenAI's ChatGPT.

Copy any study material to your clipboard, run the script, and get a ready-to-import flashcard file.

## Prerequisites

- Python 3.8+
- An [OpenAI API key](https://platform.openai.com/api-keys)

## Installation

```bash
git clone https://github.com/your-username/chatgpt-flashcards.git
cd chatgpt-flashcards
pip install -r requirements.txt
```

Create a `.env` file (or export the variable directly):

```bash
cp .env.example .env
# Edit .env and add your API key
```

## Usage

1. Copy the text you want to turn into flashcards to your clipboard.
2. Run the script:

```bash
python main.py
```

Flashcards are saved to `output.txt` by default.

### Options

```
-o, --output FILE   Output file path (default: output.txt)
-m, --model MODEL   OpenAI model to use (default: gpt-4)
```

Example:

```bash
python main.py -o biology_cards.txt -m gpt-4o
```

## Output Format

The generated file contains semicolon-separated Q&A pairs, one per line:

```
What is mitosis?;The process of cell division that results in two identical daughter cells
What is osmosis?;The movement of water molecules through a semipermeable membrane
```

This format can be imported directly into Anki using **File > Import** with the semicolon separator.

## License

[MIT](LICENSE)
