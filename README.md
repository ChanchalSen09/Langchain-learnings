# LangChain + Ollama Starter

This project uses your local `Ollama` model with `LangChain`, so you do not need an OpenAI API key.

## Prerequisites

- Ollama installed and running
- Model available locally: `llama3.2:3b`
- Python 3.10+

## Install

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Make sure Ollama is running

In another terminal:

```bash
ollama run llama3.2:3b
```

Or start the server directly:

```bash
ollama serve
```

## Run examples

Simple chat:

```bash
python chat_example.py
```

Prompt template example:

```bash
python app.py
```
