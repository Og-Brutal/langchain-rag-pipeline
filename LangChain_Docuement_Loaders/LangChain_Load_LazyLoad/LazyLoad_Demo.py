from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


BASE = Path(__file__).parent.parent / "LangChain_PDFLoader"

loader=PyPDFLoader(file_path=BASE / "dl-curriculum.pdf")

docs=loader.lazy_load()

for d in docs:
    print("\n\n MetaData : ", d.metadata)



