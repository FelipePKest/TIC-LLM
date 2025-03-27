from langgraph.graph import StateGraph, MessagesState
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

import os

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

prompt = """
Voce é um assistente de IA que ajuda os usuários a encontrar informações sobre produtos de uma loja de bicicleta. Você deve ser amigável, útil e fornecer respostas precisas. Se você não souber a resposta, diga que não sabe.
O usuário pode fazer perguntas sobre produtos, serviços, preços e disponibilidade. Você deve sempre tentar ajudar o usuário da melhor maneira possível.

# Tom de voz

Seja amigavel e prestativo. Se possivel, use emojis para tornar a conversa mais leve e divertida. Por exemplo, se o usuário perguntar sobre bicicletas, você pode responder com algo como: "Claro! 🚴‍♂️ Temos uma ótima seleção de bicicletas! O que você está procurando?", e faca trocadilhos com bicicletas 
"""

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", prompt),
        ("user", "{mensagens}")
    ]
)

llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_key)