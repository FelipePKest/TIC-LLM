from langchain_openai import ChatOpenAI
import os


chat = ChatOpenAI()

for bloco in chat.stream("Me conte uma piada de uma frase"):
    print(bloco.content, end=" ", flush=True)