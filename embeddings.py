import pickle

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from catalog import load_catalog
from config import (
    EMBEDDING_MODEL,
    FAISS_INDEX_PATH,
    METADATA_PATH,
)

# Load embedding model
model = SentenceTransformer(EMBEDDING_MODEL)


def build_text(record):
    """
    Convert one SHL assessment into searchable text.
    """

    return f"""
    Name: {record.get("name", "")}
    Description: {record.get("description", "")}
    Job Levels: {", ".join(record.get("job_levels", []))}
    Languages: {", ".join(record.get("languages", []))}
    Duration: {record.get("duration", "")}
    Category: {", ".join(record.get("keys", []))}
    Remote Testing: {record.get("remote", "")}
    Adaptive: {record.get("adaptive", "")}
    """.strip()


def build_index():
    catalog = load_catalog()

    documents = [build_text(item) for item in catalog]

    print(f"Creating embeddings for {len(documents)} assessments...")

    embeddings = model.encode(
        documents,
        convert_to_numpy=True,
        show_progress_bar=True,
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings.astype(np.float32))

    faiss.write_index(index, str(FAISS_INDEX_PATH))

    with open(METADATA_PATH, "wb") as f:
        pickle.dump(catalog, f)

    print("===================================")
    print("FAISS index created successfully!")
    print(f"Assessments indexed: {len(catalog)}")
    print(f"Embedding dimension: {dimension}")
    print("===================================")


if __name__ == "__main__":
    build_index()