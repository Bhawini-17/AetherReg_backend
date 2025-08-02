# vector_store.py

import os
import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
from obligation_schema import ObligationMetadata

class VectorStore:
    def __init__(self, index_path="vector_store/index.faiss", metadata_path="vector_store/metadata.pkl"):
        self.index_path = index_path
        self.metadata_path = metadata_path
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.metadata = []

        os.makedirs(os.path.dirname(index_path), exist_ok=True)

        if os.path.exists(self.index_path) and os.path.exists(self.metadata_path):
            self._load()

    def _load(self):
        self.index = faiss.read_index(self.index_path)
        with open(self.metadata_path, "rb") as f:
            self.metadata = pickle.load(f)

    def _save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.metadata_path, "wb") as f:
            pickle.dump(self.metadata, f)

    async def index_obligations(self, obligations: list[ObligationMetadata]):
        texts = [ob.obligation_text for ob in obligations]
        embeddings = self.model.encode(texts, convert_to_numpy=True)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        self.metadata = obligations

        self._save()
        print("📦 Obligations indexed and saved.")

    def search(self, query: str, top_k: int = 5):
        if not self.index:
            self._load()
        if not self.index:
            return []

        query_embedding = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append(self.metadata[idx])

        return results
