from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0.7)

parser=StrOutputParser()

loader=PyPDFLoader(file_path="dl-curriculum.pdf")

docs=loader.load()


print("Total Pages : ", len(docs))
print("\n\n Content on Page 1 : ", docs[0].page_content)
print("\n\n MetaData of Page 1 : ", docs[0].metadata)