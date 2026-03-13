import argparse
import sys
import os

import clipboard
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

load_dotenv()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate Anki flashcards from clipboard content using ChatGPT."
    )
    parser.add_argument(
        "-o", "--output",
        default="output.txt",
        help="Output file path (default: output.txt)",
    )
    parser.add_argument(
        "-m", "--model",
        default="gpt-4",
        help="OpenAI model to use (default: gpt-4)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Set it via 'export OPENAI_API_KEY=your-key' or add it to a .env file.")
        sys.exit(1)

    clipboard_content = clipboard.paste()
    if not clipboard_content or not clipboard_content.strip():
        print("Error: Clipboard is empty. Copy some text before running this script.")
        sys.exit(1)

    print(f"Read {len(clipboard_content)} characters from clipboard.")
    print(f"Generating flashcards using {args.model}...")

    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model=args.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a technical assistant that helps develop training materials to help pass exams.",
                },
                {
                    "role": "user",
                    "content": (
                        "Create anki flashcards with the following text using a format "
                        "like question;answer next line question;answer etc...\n\n"
                        f"{clipboard_content}"
                    ),
                },
            ],
            temperature=0.7,
            max_tokens=2000,
        )
    except OpenAIError as e:
        print(f"Error communicating with OpenAI API: {e}")
        sys.exit(1)

    generated_flashcards = response.choices[0].message.content

    with open(args.output, "w") as f:
        f.write(generated_flashcards)

    print(f"Flashcards saved to '{args.output}'")


if __name__ == "__main__":
    main()
