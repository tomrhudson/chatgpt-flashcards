import os
import openai
import clipboard

# Establish var for OpenAI API Key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Obtain content from clipboard
clipboard_content = clipboard.paste()

# Send prompts to ChatGPT engine
messages = [
    {"role": "system", "content": "You are a technical assistance that helps develop training materials to help pass exams."},
    {"role": "user", "content": f"Create anki flashcards with the following text using a format like question;answer next line question;answer etc...{clipboard_content}."}
]

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
    temperature=0.7,
    max_tokens=2000
)

generated_flashcards = response["choices"][0]["message"]["content"]

# Save flashcards to a file
with open("output.txt", "w") as f:
    f.write(generated_flashcards)

print("Flashcards saved to 'output.txt'")