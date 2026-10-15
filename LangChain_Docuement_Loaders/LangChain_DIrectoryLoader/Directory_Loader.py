from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader=DirectoryLoader(
    path="Data",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

docs=loader.load()

print("Total Pages : ", len(docs))

vector_DB_PDF=[doc for doc in docs if doc.metadata['source'].endswith('b.pdf')]


print("\n\n Total Pages in vector_DB.pdf : ", len(vector_DB_PDF))
print("\n\n Content on Page 1 of vector_DB.pdf : ", vector_DB_PDF[0].page_content)
print("\n\n MetaData of Page 1 of Vector_DB.pdf : ", vector_DB_PDF[0].metadata)



# ================= Glob Patterns (DirectoryLoader) =================
#
# Glob Pattern     | What It Loads
# -----------------|-----------------------------------------------
# "**/*.txt"       | All .txt files in all subfolders
# "*.pdf"          | All .pdf files in the root directory
# "data/*.csv"     | All .csv files in the data/ folder
# "**/*"           | All files (any type, all folders)
#
# ** = recursive search through subfolders
# ===================================================================