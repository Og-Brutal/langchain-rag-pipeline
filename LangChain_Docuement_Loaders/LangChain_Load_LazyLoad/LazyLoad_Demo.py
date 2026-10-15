from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path


BASE = Path(__file__).parent.parent / "LangChain_PDFLoader"

loader=PyPDFLoader(file_path=BASE / "dl-curriculum.pdf")

docs=loader.lazy_load()

for d in docs:
    print("\n\n MetaData : ", d.metadata)



