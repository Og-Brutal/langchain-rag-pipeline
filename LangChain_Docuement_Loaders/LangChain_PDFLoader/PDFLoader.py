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





# ================= PDF Loaders (Revision Notes) =================
#
# WHAT PDF LOADERS DO:
#   - Extract the TEXT layer of each page.
#   - Usually return 1 Document per page (page_content + metadata).
#   - Images are ignored, and text INSIDE images is not read.
#   - Scanned PDFs (pages are pictures of text) return empty or almost
#     empty page_content unless OCR is used.
#
# QUICK CHECK:
#   print(docs[0].page_content)
#   If it is blank or garbled, the PDF is probably scanned -> needs OCR.
#
# LOADERS COMPARISON:
#   PyPDFLoader           -> simple text PDFs, easiest, good for learning
#   PyMuPDFLoader         -> general use, fast, good extraction, richer
#                            metadata (author, title, page). Best default.
#   PDFPlumberLoader      -> PDFs with TABLES (keeps layout/structure better)
#   UnstructuredPDFLoader -> scanned PDFs / complex layouts, uses OCR
#                            (needs Tesseract), heavier and slower
#   PyPDFium2Loader       -> fast, lightweight, accurate on clean PDFs
#
# HOW TO CHOOSE:
#   Normal text PDF (notes, books, papers) -> PyMuPDFLoader
#   PDF with tables                        -> PDFPlumberLoader
#   Scanned PDF (images of text)           -> UnstructuredPDFLoader (OCR)
#   Just learning                          -> PyPDFLoader
#
# USAGE (same for all):
#   from langchain_community.document_loaders import PyMuPDFLoader
#   loader = PyMuPDFLoader("file.pdf")
#   docs = loader.load()
#   len(docs)   -> number of pages
#
# INSTALL THE NEEDED PACKAGE:
#   pip install pypdf        (PyPDFLoader)
#   pip install pymupdf      (PyMuPDFLoader)
#   pip install pdfplumber   (PDFPlumberLoader)
#
# OCR FOR IMAGES INSIDE A PDF (PyPDFLoader):
#   loader = PyPDFLoader("file.pdf", extract_images=True)
#   needs: pip install rapidocr-onnxruntime
#   - Only reads WORDS inside images, does not understand photos or charts.
#   - Parameter may vary by langchain-community version, check the docs.
#
# UNDERSTANDING IMAGES (charts, diagrams, photos):
#   Needs a multimodal model (e.g. Gemini) that receives the page images
#   and describes them. This is a more advanced RAG setup.
#
# TIP:
#   Load the same PDF with two loaders and compare page_content.
#   Pick whichever gives cleaner text, since quality varies per PDF.
#
# ONE-LINER: PDF loaders read text only; pick the loader by PDF type
#            (text -> PyMuPDF, tables -> PDFPlumber, scanned -> Unstructured OCR).
# ================================================================