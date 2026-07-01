import pickle

import faiss
from sentence_transformers import SentenceTransformer

from config import (
    EMBEDDING_MODEL,
    FAISS_INDEX_PATH,
    METADATA_PATH,
)

# -----------------------------
# Load Embedding Model
# -----------------------------

model = SentenceTransformer(EMBEDDING_MODEL)

# -----------------------------
# Load FAISS Index
# -----------------------------

index = faiss.read_index(str(FAISS_INDEX_PATH))

# -----------------------------
# Load Assessment Metadata
# -----------------------------

with open(METADATA_PATH, "rb") as f:
    catalog = pickle.load(f)


# -----------------------------
# Semantic Search
# -----------------------------

def search_assessments(query, top_k=10):
    """
    Perform semantic search over SHL assessments.

    Returns:
        results : List[dict]
            Matching assessment metadata.

        scores : List[float]
            Similarity scores from FAISS.
    """

    query_embedding = model.encode([query])

    scores, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:

        if idx == -1:
            continue

        results.append(catalog[idx])

    return results


# -----------------------------
# Test Search
# -----------------------------

if __name__ == "__main__":

    query = input("Enter search query: ")

    results = search_assessments(query)

    print("\nTop Results\n")

    for i, item in enumerate(results, 1):

        print("=" * 60)
        print(f"{i}. {item['name']}")
        print(item["description"])
        print(item["link"])