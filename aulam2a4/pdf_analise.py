from langchain.document_loaders import PyPDFLoader

# Carregar o documento PDF
loader = PyPDFLoader("clima_brasil.pdf")
docs = loader.load()

# Concatenar todo o texto
text = "\n\n".join([doc.page_content for doc in docs])

print(text)
