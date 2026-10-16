from langchain_community.retrievers import WikipediaRetriever
import wikipedia
wikipedia.set_user_agent("RAGLearningApp/1.0 (f233043@cfd.nu.edu.pk)")

retriever=WikipediaRetriever(top_k_results=2,lang="en")

querry="articles on Ai Agents"
docs=retriever.invoke(querry)

print("Total Similar Documents : ",len(docs))
print("\n\n Document 1 Page Content : ",docs[0].page_content)
print("\n\n Document 1 Meta Data : ",docs[0].metadata)
