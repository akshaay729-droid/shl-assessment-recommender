import pickle

import faiss
from sentence_transformers import SentenceTransformer

from config import (
    EMBEDDING_MODEL,
    FAISS_INDEX_PATH,
    METADATA_PATH,
)

# Load embedding model
model = SentenceTransformer(EMBEDDING_MODEL)

# Load FAISS index
index = faiss.read_index(str(FAISS_INDEX_PATH))

# Load assessment metadata
with open(METADATA_PATH, "rb") as f:
    catalog = pickle.load(f)


def search_assessments(query, top_k=10):
    """
    Semantic search over SHL assessments.
    """

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        if idx == -1:
            continue

        results.append(catalog[idx])

    return results


if __name__ == "__main__":

    query = input("Enter search query: ")

    results = search_assessments(query)

    print("\nTop Results\n")

    for i, item in enumerate(results, 1):

        print("=" * 50)

        print(f"{i}. {item['name']}")

        print(item["description"])

        print(item["link"])