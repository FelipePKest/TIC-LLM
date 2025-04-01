import streamlit as st
from langchain_community.document_loaders import PyPDFLoader  # PyMuPDF para leitura de PDFs
from chatbot_com_contexto import app
from langchain_core.messages import AIMessage, HumanMessage
# from chatbot_prompt import get_llm_with_prompt
from langgraph.graph import StateGraph, MessagesState

st.set_page_config(layout='wide', page_title='Chatbot de loja de bicicletas', page_icon='🚴')

st.title("Loja de Bicicletas - Assistente Virtual")

if 'message_history' not in st.session_state:
    st.session_state.message_history = [AIMessage(content="Olá, sou um assistente virtual para ajudar você a encontrar informações sobre produtos de uma loja de bicicleta. Como posso ajudar você hoje?")]

# Upload de PDF
uploaded_file = st.file_uploader("Faça o upload de um PDF para análise", type=["pdf"])

pdf_text = ""
if uploaded_file is not None:
    file_name = uploaded_file.name
    pdf_loader = PyPDFLoader(file_name)
    docs = pdf_loader.load()
    pdf_text = "\n\n".join(doc.page_content for doc in docs)
    
# Entrada do usuário
user_input = st.chat_input("Digite aqui...")

if user_input:
    st.session_state.message_history.append(HumanMessage(content=user_input))
    
    response = app.invoke({
        'question': user_input,
        'context': [{'page_content': pdf_text}]
    })
    
    st.session_state.message_history.append(AIMessage(content=response['answer']))

# Exibição das mensagens
for i in range(1, len(st.session_state.message_history) + 1):
    this_message = st.session_state.message_history[-i]
    if isinstance(this_message, AIMessage):
        message_box = st.chat_message('assistant')
    else:
        message_box = st.chat_message('user')
    message_box.markdown(this_message.content)
