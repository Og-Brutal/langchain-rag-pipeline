from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader(file_path="cricket.txt", encoding="utf-8")


docs=loader.load()

print(docs)

print("\n Type : ", type(docs))

print("\n Length : ", len(docs))

print("\n Type of Content : ", type(docs[0].page_content))

print("\n Content : ", docs[0].page_content[:200])

print("\n Metadata : ", docs[0].metadata)


prompt=PromptTemplate(
    template="Summarize the following Poem:\n\n{Poem}",
    input_variables=["Poem"],
)

parser=StrOutputParser()

llm=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0.7)

chain=prompt | llm | parser

print("\n\n Summarized Poem : ", chain.invoke(docs[0].page_content))

# Role of encoding="utf-8"
# A text file is stored as bytes, and the encoding tells Python how to turn
# those bytes into characters. utf-8 is the standard encoding that supports
# almost every language and symbol (English, Urdu, emojis, accented letters, etc.).
#
# loader = TextLoader("notes.txt", encoding="utf-8")
#
# If you leave it out, TextLoader uses your system's default encoding.
# That is usually fine on Linux (which defaults to UTF-8), but on Windows it
# can be something else, like cp1252. Then a file with special characters
# can fail with:
#
# UnicodeDecodeError: 'charmap' codec can't decode byte ...