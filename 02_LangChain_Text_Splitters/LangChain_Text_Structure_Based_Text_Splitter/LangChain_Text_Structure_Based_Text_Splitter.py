from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """My name is Nitish
I am 35 years old

I live in Gurgaon
How are you"""


# smaller_chunk size=10
text_splitter_case_1 = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
)

result=text_splitter_case_1.split_text(text)
print(result)

# in this case chunk size is 25 so it will not split the text into smaller chunks because the text is less than 25 characters
text_splitter_case_2 = RecursiveCharacterTextSplitter(
    chunk_size=25,
    chunk_overlap=0,
)
result=text_splitter_case_2.split_text(text)
print(result)


# now third case >=50

text_splitter_case_3 = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0,
)
result=text_splitter_case_3.split_text(text)
print(result)
