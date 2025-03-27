from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
import langchain
import getpass
import os

if not os.environ.get("OPENAI_API_KEY"):
 os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")


model = init_chat_model("gpt-4o-mini", model_provider="openai")

messages = [
   SystemMessage("Traduza o seguinte texto de Ingles para Portugues"),
   HumanMessage("hi!"),
]

response = model.invoke(messages)
print(response.content)


system_template = "Traduza o seguinte texto de Ingles para {idioma}"

prompt_template = ChatPromptTemplate.from_messages(
   [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"idioma": "Italian", "text": "hi!"})
response = model.invoke(prompt)

print(response.content)
