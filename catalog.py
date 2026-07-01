import json
from pathlib import Path

CATALOG_PATH = Path("data/catalog.json")


def load_catalog():
    """Load the SHL assessment catalog."""
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_catalog_size():
    return len(load_catalog())


if __name__ == "__main__":
    catalog = load_catalog()

    print(f"✅ Loaded {len(catalog)} assessments")
    print(f"First assessment: {catalog[0]['name']}")