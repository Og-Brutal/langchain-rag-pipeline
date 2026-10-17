from langchain_community.document_loaders import CSVLoader


loader=CSVLoader(file_path="Social_Network_Ads.csv")

docs=loader.load()


print("Total Pages : ", len(docs))

print("\n\n Content of first row : ", docs[0].page_content)
print("\n\n MetaData of first row : ", docs[0].metadata)
print("\n\n Content of second row : ", docs[1].page_content)
print("\n\n MetaData of second row : ", docs[1].metadata)
