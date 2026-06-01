import streamlit as st
from rag_engine import ask_question

st.title("🏛️ Nubian Chronicles AI Heritage Guide")

st.write(
    "Proof-of-concept AI heritage character "
    "for digital heritage environments."
)

question = st.text_input(
    "Ask a question:"
)

if st.button("Ask"):

    if question:

        answer = ask_question(question)

        st.subheader("AI Character Response")

        st.success(answer)
