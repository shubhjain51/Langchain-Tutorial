# app.py

import streamlit as st
from llm_chain import ask_question

st.set_page_config(page_title="Gemini LLM App", page_icon="🧠")
st.title("💬 Ask Me Anything (Gemini-Powered)")

question = st.text_input("Ask a question:")

if st.button("Get Answer"):
    if question.strip():
        with st.spinner("Thinking..."):
            try:
                response = ask_question(question)
                st.success("Gemini says:")
                st.markdown(response)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter a question.")
