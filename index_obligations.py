import os
import faiss
import pickle
import asyncio
from sentence_transformers import SentenceTransformer
from database.obligation_repository import ObligationRepository
from obligation_schema import ObligationMetadata

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# FAISS setup
embedding_dim = 384
index = faiss.IndexFlatL2(embedding_dim)
obligation_texts = []
metadata_list = []

async def index_obligations():
    repo = ObligationRepository()
    obligations = await repo.get_all_obligations()
    
    for doc in obligations:
        text = doc.get("obligation_text")
        if not text:
            continue

        embedding = model.encode([text])
        index.add(embedding)
        obligation_texts.append(text)
        metadata_list.append(doc)

    # Save index and metadata
    faiss.write_index(index, "faiss_obligation.index")
    with open("obligation_metadata.pkl", "wb") as f:
        pickle.dump(metadata_list, f)

    print(f"✅ Indexed {len(obligation_texts)} obligations into FAISS.")

if __name__ == "__main__":
    asyncio.run(index_obligations())
