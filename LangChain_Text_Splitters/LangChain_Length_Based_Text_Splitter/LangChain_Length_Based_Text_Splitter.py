from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader(file_path="dl-curriculum.pdf")

# The loader gives 1 Document per page.
# Example: if the PDF has 23 pages, docs will contain 23 Documents.
docs = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size=500,     # max characters per chunk
    chunk_overlap=50,   # characters shared between neighbouring chunks
    separator=""        # split purely by length
)

# Chunking: the splitter treats each Document (page) as ONE text string
# and splits it separately into smaller Documents (chunks).
# So 23 page-Documents become many smaller chunk-Documents.
# Chunks never span two pages, and each chunk keeps its page's metadata
# (source, page, ...).
result = text_splitter.split_documents(docs)


print("Total Pages : ", len(docs))                       # e.g. 23
print("\n\n Total Chunks : ", len(result))                # much more than 23
print("\n\n length of first chunk : ", len(result[0].page_content))
print("\n\n Content of first chunk : ", result[0].page_content)