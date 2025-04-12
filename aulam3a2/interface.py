import streamlit as st
import fitz  # PyMuPDF para leitura de PDFs
from chatbot import app
from langchain_core.messages import AIMessage, HumanMessage

from dotenv import load_dotenv

load_dotenv()

st.set_page_config(layout='wide', page_title='Chatbot de loja de bicicletas', page_icon='🚴')

st.title("Loja de Bicicletas - Assistente Virtual")

if 'message_history' not in st.session_state:
    st.session_state.message_history = [AIMessage(content="Olá, sou um assistente virtual para ajudar você a encontrar informações sobre produtos de uma loja de bicicleta. Como posso ajudar você hoje?")]

# Entrada do usuário
user_input = st.chat_input("Digite aqui...")

if user_input:
    st.session_state.message_history.append(HumanMessage(content=user_input))
    
    response = app.invoke({
        'messages': st.session_state.message_history
    })
    
    st.session_state.message_history = response['messages']

# Exibição das mensagens
for i in range(1, len(st.session_state.message_history) + 1):
    this_message = st.session_state.message_history[-i]
    if isinstance(this_message, AIMessage):
        message_box = st.chat_message('assistant')
    else:
        message_box = st.chat_message('user')
    message_box.markdown(this_message.content)
