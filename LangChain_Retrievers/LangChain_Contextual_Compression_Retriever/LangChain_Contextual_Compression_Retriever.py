from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv


load_dotenv()


# Recreate the document objects from the previous data
docs = [
    Document(page_content=(
        """The Grand Canyon is one of the most visited natural wonders in the world.
        Photosynthesis is the process by which green plants convert sunlight into energy.
        Millions of tourists travel to see it every year. The rocks date back millions of years."""
    ), metadata={"source": "Doc1"}),

    Document(page_content=(
        """In medieval Europe, castles were built primarily for defense.
        The chlorophyll in plant cells captures sunlight during photosynthesis.
        Knights wore armor made of metal. Siege weapons were often used to breach castle walls."""
    ), metadata={"source": "Doc2"}),

    Document(page_content=(
        """Basketball was invented by Dr. James Naismith in the late 19th century.
        It was originally played with a soccer ball and peach baskets. NBA is now a global league."""
    ), metadata={"source": "Doc3"}),

    Document(page_content=(
        """The history of cinema began in the late 1800s. Silent films were the earliest form.
        Thomas Edison was among the pioneers. Photosynthesis does not occur in animal cells.
        Modern filmmaking involves complex CGI and sound design."""
    ), metadata={"source": "Doc4"})
]


vector_store=FAISS.from_documents(
    embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"),
    documents=docs
)

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0.7)
compressor=LLMChainExtractor.from_llm(llm)

retiever=vector_store.as_retriever(search_kwargs={"k":2})
raw=retiever.invoke("What Is Photosynthesis ?")
contextual_compressor_retriever=ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retiever
)

querry="what is Photosynthesis ?"

res=contextual_compressor_retriever.invoke(querry)

raw = retiever.invoke(querry)
for doc in raw:
    print("\nRETRIEVED:", doc.metadata["source"])
    print(doc.page_content)

print("\n--- AFTER COMPRESSION ---")
for doc in res:
    print(doc.metadata["source"], ":", doc.page_content)

