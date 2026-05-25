# LLM-Text-Summarizer
A lightweight local LLM text summarizer powered by Ollama.


# ✂️ LLM Text Summarizer

> A local AI-powered text summarization app built with **Streamlit** and **Ollama (LLaMA 3)**. Runs entirely on your machine — no API keys, no internet required.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-LLaMA%203-black?logo=ollama)


---

## 📌 Overview

This project demonstrates the integration of a **locally hosted Large Language Model (LLM)** with a Python web application. Users can paste any text and receive a concise, under-20-word summary powered by Meta's **LLaMA 3** model running locally via **Ollama**.

The app is designed to be lightweight, privacy-preserving, and easy to run without any cloud dependencies.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend / UI** | Streamlit |
| **LLM Runtime** | Ollama |
| **Model** | LLaMA 3 (8B) |
| **Prompt Engineering** | Custom prompt template module |
| **Language** | Python 3.10+ |

---

## 🚀 Features

- 📄 **Text summarization** under 20 words using LLaMA 3
- ⚡ **Fully local inference** — no OpenAI key, no internet required
- 🎯 **Prompt template module** for clean separation of concerns
- 📥 **Download summary** as a `.txt` file
- 📊 Live word/character counter

---

## 📂 Project Structure

```
llm-text-summarizer/
├── src/
│   ├── app.py          # Main Streamlit application
│   └── prompt.py       # Prompt template module
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com/) installed on your machine

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/llm-text-summarizer.git
cd llm-text-summarizer
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Pull the LLaMA 3 model via Ollama

```bash
ollama pull llama3
```

### 4. Run the app

```bash
streamlit run src/app.py
```

Open your browser at `http://localhost:8501`

---

## 🧠 How It Works

```
User Input (Text)
       ↓
Prompt Template (prompt.py)
       ↓
Ollama API (Local LLaMA 3)
       ↓
LLM Response → Display in Streamlit UI
```

1. The user enters text in the Streamlit text area.
2. The text is inserted into a structured prompt template that instructs the model to summarize under 20 words.
3. The prompt is sent to the local Ollama instance via the `ollama` Python client.
4. The model's response is displayed in the UI and optionally downloaded.

---

## 💡 Key Design Decisions

- **Modular prompt file**: Keeping the prompt in a separate `prompt.py` module makes it easy to swap, version, or extend prompts without touching the UI code.
- **Local LLM (Ollama)**: Avoids API cost, latency, and privacy concerns associated with cloud-based LLMs.
- **Streamlit**: Enables rapid prototyping of ML/AI apps with minimal boilerplate.

---


## 🔮 Future Improvements

- [ ] Model selector (LLaMA 3, Mistral, Gemma)
- [ ] Adjustable summary length slider
- [ ] Batch file upload for multi-document summarization
- [ ] Summary history / session log
- [ ] Export to PDF

---

