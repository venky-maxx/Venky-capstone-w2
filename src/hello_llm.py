import sys
from dotenv import load_dotenv
from openai import OpenAI

sys.stdout.reconfigure(encoding='utf-8')

# Load OPENAI_API_KEY from .env if a .env file exists.

load_dotenv()

# Create the OpenAI client — it reads OPENAI_API_KEY from the environment automatically.
client = OpenAI()


def ask(question: str) -> str:
    """Send one question to the LLM and return the answer text."""
    resp = client.chat.completions.create(
        model="gpt-5.2",
        messages=[
            {"role": "system", "content": "You are concise."},
            {"role": "user",   "content": question},
        ],
        temperature=0.3,
    )
    return resp.choices[0].message.content

sys.stdout.reconfigure(encoding='utf-8')

if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "Say hello in one sentence."
    print(ask(q))
    # replace with print(strip_markdown(ask(q))) to get file in txt format.

