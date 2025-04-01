import pypdf
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain.document_loaders import PyPDFLoader
from langgraph.graph import StateGraph, MessagesState
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

class State(dict):
    pergunta: str
    contexto: list
    resposta: str


template = """
Responda a pergunta abaixo com base no contexto fornecido. Se a pergunta não puder ser respondida com o contexto, diga que não sabe. Seja amigável e útil.:
{contexto}

{pergunta}

Answer:
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["pergunta", "contexto"],
)


llm = ChatOpenAI(model="gpt-4o-mini")


qna_chain = prompt | llm

graph_builder = StateGraph(State)

def generate(state: State):
    # Concatenar todo o texto
    docs_content = "\n\n".join(doc.page_content for doc in state["contexto"])
    response = qna_chain.invoke({"pergunta": state["pergunta"], "contexto": docs_content})
    return {"resposta": response.content}

graph_builder.add_node("generate", generate)


graph_builder.set_entry_point("generate")
graph_builder.set_finish_point("generate")

app = graph_builder.compile()

loader = PyPDFLoader("aulam2a4/clima_brasil.pdf")
docs = loader.load()

# Concatenar todo o texto
contexto = docs

pergunta = "Qual é o principal argumento do documento?"

# # Rodar o grafo
response = app.invoke({"contexto":contexto, "pergunta":pergunta})  # Passa contexto e pergunta

print(response["resposta"])  # Imprime a resposta
