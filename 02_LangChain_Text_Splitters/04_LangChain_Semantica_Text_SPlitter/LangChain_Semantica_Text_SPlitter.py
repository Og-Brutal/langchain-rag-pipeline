from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.


Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

chunker = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1,   
)


docs=chunker.create_documents([sample])

print("Total Chunks : ", len(docs))
print("\n\n Chunks : ", docs  )


# ===== Standard Deviation in SemanticChunker =====
#
# 1. We calculate the cosine distance between every pair of neighbouring
#    sentences. A small distance means same topic, a big distance means
#    the topic changed.
#
# 2. Mean of all distances = the typical (normal) distance between
#    neighbouring sentences in this document.
#
# 3. Standard deviation (SD) of all distances = how much a distance
#    normally deviates from that mean. It tells us what normal variation
#    looks like for this document.
#
# 4. breakpoint_threshold_amount = how many SDs above the mean a distance
#    must be before we call it a real topic change (a split point).
#
#       threshold = mean + (amount * SD)
#       distance > threshold  -->  split here
#
#
# 5. Tuning:
#       lower amount  -> lower threshold -> MORE splits (small chunks)
#       higher amount -> higher threshold -> FEWER splits (big chunks)
#
#    Note: with a high amount (like 3) on a short text, no distance may
#    reach the threshold, so you get a single chunk.
# ==================================================