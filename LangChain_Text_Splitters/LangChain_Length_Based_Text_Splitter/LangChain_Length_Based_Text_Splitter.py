from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader(file_path="dl-curriculum.pdf")

docs=loader.load()

text_splitter=CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separator=""
)

result=text_splitter.split_documents(docs)


print("Total Pages : ", len(docs))
print("\n\n Total Chunks : ", len(result))
print("\n\n length of first chunk : ", len(result[0].page_content))
print("\n\n Content of first chunk : ", result[0].page_content)
