import streamlit as st
from langchain.llms import OpenAI

# Configuração da interface
st.title("Chat com IA usando LangChain")
prompt = st.text_area("Digite sua pergunta:")

if st.button("Enviar"):
    if prompt:
        llm = OpenAI()
        resposta = llm(prompt)
        st.write("**Resposta:**", resposta)
    else:
        st.warning("Digite uma pergunta antes de enviar.")
