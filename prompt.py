"""
Prompt templates for the LLM Text Summarizer.
"""

SUMMARIZE_PROMPT = """You are an expert text summarizer.

Instructions:
- Keep the summary under 20 words
- Preserve key points
- Use simple language

Text:
{}
"""
