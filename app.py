import streamlit as st
import ollama
from prompt import SUMMARIZE_PROMPT

# --- Page Config ---
st.set_page_config(
    page_title="LLM Text Summarizer",
    page_icon="✂️",
    layout="centered"
)

# --- UI ---
st.title("✂️ LLM Text Summarizer")
st.caption("Powered by LLaMA 3 via Ollama — summarizes any text in under 20 words.")

st.divider()

text = st.text_area(
    "Enter your text below:",
    height=200,
    placeholder="Paste any article, paragraph, or passage here..."
)

col1, col2 = st.columns([1, 4])

with col1:
    summarize_btn = st.button("Summarize", type="primary", use_container_width=True)

with col2:
    if text:
        st.caption(f"📝 {len(text.split())} words · {len(text)} characters")

st.divider()

if summarize_btn:
    if not text.strip():
        st.warning("Please enter some text before summarizing.")
    else:
        final_prompt = SUMMARIZE_PROMPT.format(text)

        with st.spinner("Thinking..."):
            try:
                response = ollama.chat(
                    model='llama3',
                    messages=[
                        {
                            'role': 'user',
                            'content': final_prompt
                        }
                    ]
                )
                summary = response['message']['content']

                st.success("Summary")
                st.write(summary)

                st.download_button(
                    label="Download Summary",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error connecting to Ollama: {e}")
                st.info("Make sure Ollama is running locally with LLaMA 3 pulled. Run: `ollama pull llama3`")
