import uuid

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph


model = ChatOpenAI(model="gpt-4o-mini")

# Definimos o grafo de estados para coordenarmos as mensagens
workflow = StateGraph(state_schema=MessagesState)


# Como chamaremos o modelo com as mensagens
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}


# Definindo os estados da conversa
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# O armazenamento da memoria da conversa
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# Definindo o ID da conversa pela thread
thread_id = uuid.uuid4()
config = {"configurable": {"thread_id": thread_id}}

query = "Olá, eu sou o Felipe!"

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()

query = "Como eu me chamo?"

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()
# for event in app.stream({"messages": input_messages}, config, stream_mode="values"):
#     event["messages"][-1].pretty_print()