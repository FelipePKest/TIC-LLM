from langgraph.graph import StateGraph, MessagesState
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

import os

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

template = """
Responda a pergunta abaixo com base no contexto fornecido. Se a pergunta não puder ser respondida com o contexto, diga que não sabe. Seja amigável e útil.:
{context}

{question}

Answer:
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["question", "context"],
)


llm = ChatOpenAI(api_key=openai_key, model="gpt-4o-mini")


qna_chain = prompt | llm

class State(dict):
    question: str
    context: list
    answer: str

graph_builder = StateGraph(State)

def generate(state: State):
    docs_content = "\n\n".join(doc["page_content"] for doc in state["context"])
    response = qna_chain.invoke({"question": state["question"], "context": docs_content})
    return {"answer": response.content}

graph_builder.add_node("generate", generate)


graph_builder.set_entry_point("generate")
graph_builder.set_finish_point("generate")

app = graph_builder.compile()