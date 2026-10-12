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

print("\n Content : ", docs[0].page_content)

print("\n Metadata : ", docs[0].metadata)


prompt=PromptTemplate(
    template="Summarize the following Poem:\n\n{Poem}",
    input_variables=["Poem"],
)

parser=StrOutputParser()

llm=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0.7)

chain=prompt | llm | parser

print("\n\n Summarized Poem : ", chain.invoke(docs[0].page_content))