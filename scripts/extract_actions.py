from groq import Groq
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def extract_action_items(text):
    """
    Extract action items using Groq LLaMA model
    """
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set.")

    client = Groq(api_key=api_key)
    
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant that extracts action items from meeting transcripts. "
                    "List all tasks, decisions, and action items clearly in bullet points."
                )
            },
            {
                "role": "user",
                "content": f"Extract action items from this meeting transcript:\n\n{text}"
            }
        ],
        temperature=0.1
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    input_path = "outputs/transcript.txt"
    output_path = "outputs/action_items.txt"

    if not os.path.exists(input_path):
        print(f"Transcript file not found at {input_path}")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        transcript = f.read()
    
    actions = extract_action_items(transcript)
    print(actions)

    os.makedirs("outputs", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(actions)
