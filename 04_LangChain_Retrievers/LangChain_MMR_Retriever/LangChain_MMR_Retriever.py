# Maximal Margin Relevance Retriever

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

vector_Store=FAISS.from_documents(
    documents=docs,
    embedding=embeddings,
)

retriever1=vector_Store.as_retriever(
    search_type="mmr",
    search_kwargs={"k":3,"lambda_mult":1} # k = top results, lambda_mult = relevance-diversity balance
)



# for lamda_mult=1 it will workas normal similarity search but range(0,1) place between 0,1 for diversity-relevance balance 


retriever2=vector_Store.as_retriever(
    search_type="mmr",
    search_kwargs={"k":3,"lambda_mult":0.5} # k = top results, lambda_mult = relevance-diversity balance
)
res=retriever1.invoke("what is langchain ?")

for i,doc in enumerate(res):
    print(f"Page content of Document {i+1} : \n\n",doc.page_content)

res=retriever2.invoke("what is langchain ?")

print("\n\n Trying Another Value for Lamda_Mult \n\n")
for i,doc in enumerate(res):
    print(f"Page content of Document {i+1} : \n\n",doc.page_content)


