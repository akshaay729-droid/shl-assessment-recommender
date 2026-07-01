---
title: SHL Assessment Recommender
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

# SHL Assessment Recommender

An AI-powered conversational recommender that suggests the most suitable **SHL assessments** from natural language queries.

The project combines **semantic search (FAISS + Sentence Transformers)** with **Google Gemini** to retrieve relevant SHL assessments and generate intelligent recommendations through a **FastAPI REST API**.

---

# Features

- Semantic search using FAISS
- Sentence Transformer embeddings
- Google Gemini powered recommendations
- FastAPI REST API
- Interactive Swagger UI
- Natural language assessment search
- Context-aware assessment recommendations

---

# Tech Stack

- Python
- FastAPI
- FAISS
- Sentence Transformers
- Google Gemini API

---

# Project Structure

```
shl-recommender/
│
├── app.py
├── chat.py
├── recommender.py
├── embeddings.py
├── catalog.py
├── config.py
├── prompts.py
├── utils.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── catalog.json
│
├── docs/
│   ├── swagger-home.png
│   └── python-recommendation.png
│
└── README.md
```

**Note:** `metadata.pkl` and `shl.index` are generated automatically by running `embeddings.py` and therefore are not stored in the repository.

---

# Installation

## Clone the repository

```bash
git clone https://github.com/akshaay729-droid/shl-assessment-recommender.git

cd shl-assessment-recommender
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

## Generate the FAISS index (First Run Only)

```bash
python embeddings.py
```

This command generates:

- `data/metadata.pkl`
- `data/shl.index`

## Run the application

```bash
python -m uvicorn app:app --reload
```

---

# Swagger Documentation

Open:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Health Check

**GET**

```
/health
```

Example Response

```json
{
  "status": "ok"
}
```

---

## Chat Endpoint

**POST**

```
/chat
```

Example Request

```json
{
  "message": "Recommend a Python assessment",
  "history": []
}
```

Example Response

```json
{
  "response": "Here is an assessment recommendation..."
}
```

---

# System Architecture

```
                 User Query
                      │
                      ▼
              FastAPI REST API
                      │
                      ▼
      Sentence Transformer Embedding
                      │
                      ▼
          FAISS Semantic Search
                      │
                      ▼
      Top Matching SHL Assessments
                      │
                      ▼
          Google Gemini LLM
                      │
                      ▼
      Natural Language Recommendation
```

---

# Demo

## Swagger API Documentation

![Swagger UI](docs/swagger-home.png)

---

## Example Recommendation

![Python Recommendation](docs/python-recommendation.png)

---

# Example Queries

- Recommend a Python assessment
- Java assessment under 20 minutes
- SQL assessment
- Leadership assessment
- Personality assessment for managers
- Assessment for fresh graduates
- Cognitive ability assessment

---

# Future Improvements

- Multi-turn conversation support
- Similarity threshold filtering for unrelated queries
- Hybrid keyword + semantic retrieval
- Conversation memory
- Docker support
- Cloud deployment
- Streaming responses
- Reranking of retrieved assessments

---

# Author

**Akshat Agrawal**

GitHub: https://github.com/akshaay729-droid

LinkedIn: https://www.linkedin.com/in/akshatagrawal/

---

# License

This project was developed as part of the **SHL AI Intern Take-Home Assignment**.

## Acknowledgements

- SHL Product Catalog for assessment information.
- Google Gemini API for conversational response generation.
- Sentence Transformers for semantic embeddings.
- FAISS for efficient vector similarity search.
