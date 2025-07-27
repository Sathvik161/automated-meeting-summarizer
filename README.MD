# 🤖 Automated Meeting Summarizer

The **Automated Meeting Summarizer** is a Python-based tool that allows you to upload an audio file from a meeting, automatically transcribe the content, summarize it using advanced Large Language Models (LLMs), and extract key actions discussed in the meeting.

## 🧠 Features

- 🔊 Upload meeting audio files (`.mp3`, `.wav`, etc.)
- ✍️ Transcribes speech to text
- 🧾 Summarizes the entire meeting using Groq-powered LLMs
- ✅ Extracts key action items from the conversation
- 🛠️ Easy setup with `.env` for secrets and config

---

## 🧰 Technologies Used

- **Groq API** — for high-speed LLM inference
- **Pydub** — audio processing
- **Speech Recognition** (optional) — for transcription
- **SpaCy** — NLP pipeline and entity recognition
- **Regex** — custom pattern matching for action items
- **Python-Magic** — file type detection
- **python-dotenv** — for managing secrets

---

## 📦 Requirements

Install the dependencies with:

```bash
pip install -r requirements.txt
```

##🔐 .env Setup
Create a .env file in the root with the following:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

##🚀 How to Use
Add your .env file with your Groq API key.

Run the tool with:

```bash
python pipeline.py
```
Upload your meeting audio file in the data directory.

Receive a summary and list of action items extracted from the meeting in the respective output directories.


##📝 License
MIT License

