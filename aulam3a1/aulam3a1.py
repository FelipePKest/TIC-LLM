import streamlit as st
from langchain_openai import ChatOpenAI

# Configuração da interface
st.title("Chat com IA usando LangChain")
prompt = st.text_area("Digite sua pergunta:")

if st.button("Enviar"):
    if prompt:
        llm = ChatOpenAI()
        resposta = llm.invoke(prompt+"A mensagem deve conter algo sobre a criacao do GPT2 e GPT3, indo ate tempos mais recentes, ainda destacando preocupacoes eticas em relacao ao uso das ferramentas.")
        st.write("**Resposta:**", resposta.content)
    else:
        st.warning("Digite uma pergunta antes de enviar.")
