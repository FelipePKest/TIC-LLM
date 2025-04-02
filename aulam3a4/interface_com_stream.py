import streamlit as st
import fitz  # PyMuPDF para leitura de PDFs
from chatbot_com_stream import app
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
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        pdf_text = "\n".join([page.get_text("text") for page in doc])
    
# Entrada do usuário
user_input = st.chat_input("Digite aqui...")

if user_input:
    st.session_state.message_history.append(HumanMessage(content=user_input))
    
    # Caixa de mensagem do assistente com streaming
    msg_box = st.chat_message("assistant")
    # with st.chat_message("assistant") as msg_box:
    response_stream = app.invoke({
        'question': user_input,
        'context': [{'page_content': pdf_text}]
    })["answer"]

    full_response = ""
    for chunk in msg_box.write_stream(response_stream):
        full_response += chunk

    # Salva a resposta completa
    st.session_state.message_history.append(AIMessage(content=full_response))

# Exibição das mensagens
for i in range(2,len(st.session_state.message_history)+1):
    this_message = st.session_state.message_history[-i]
    if isinstance(this_message, AIMessage):
        message_box = st.chat_message('assistant')
    else:
        message_box = st.chat_message('user')
    message_box.markdown(this_message.content)
