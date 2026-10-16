from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

vectorStore=Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="my_collection"
)

retiever=vectorStore.as_retriever(search_kwargs={"k":2})


query = "What is Chroma used for?"

res=retiever.invoke(query)

for i, doc in enumerate(res):
    print(f"Page Content {i+1} : {doc.page_content}")
    print(f"Metadata {i+1} : {doc.metadata}")