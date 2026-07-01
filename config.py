from pathlib import Path

# -----------------------
# Project Paths
# -----------------------

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"

CATALOG_PATH = DATA_DIR / "catalog.json"

FAISS_INDEX_PATH = DATA_DIR / "shl.index"

METADATA_PATH = DATA_DIR / "metadata.pkl"

# -----------------------
# Embedding Model
# -----------------------

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# -----------------------
# Recommendation Settings
# -----------------------

TOP_K = 10