from langchain_openai import ChatOpenAI
import os


chat = ChatOpenAI()


print(chat.invoke("Me conte uma piada de uma frase").content)