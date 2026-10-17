from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


url="https://lilianweng.github.io/posts/2023-06-23-agent/"

loader=WebBaseLoader(url)

docs=loader.load()

print("Total Pages : ", len(docs))
print("\n\n Content on Page 1 of WebBaseLoader : ", docs[0].page_content)
print("\n\n MetaData of Page 1 of WebBaseLoader : ", docs[0].metadata)

prompt=PromptTemplate(
    template="does blog explain the self reflection if yes then what it said :\n\n{Blog}",
    input_variables=["Blog"],
)


llm=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0.7)

parser=StrOutputParser()

chain= prompt | llm | parser

result=chain.invoke(docs[0].page_content)
print("\n\n about self reflection  : ", result)

#WEbBasedLoader uses the beautifulsoup and request library behind the scenes so it they should be in requirements file