from groq import Groq
import os
import sys
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def summarize_text(text):
    """
    Summarize text using Groq LLaMA model
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
                    "You are a helpful assistant that summarizes meeting transcripts. "
                    "Provide a concise summary focusing on key points, action items, and decisions."
                )
            },
            {
                "role": "user",
                "content": f"Summarize this meeting transcript:\n\n{text}"
            }
        ],
        temperature=0.3
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    input_path = "outputs/transcript.txt"
    output_path = "outputs/summary.txt"

    if not os.path.exists(input_path):
        print(f"Transcript file not found at {input_path}")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        transcript = f.read()
    
    summary = summarize_text(transcript)
    print(summary)

    os.makedirs("outputs", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary)
