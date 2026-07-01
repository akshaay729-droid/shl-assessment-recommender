import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors

from prompts import SYSTEM_PROMPT
from recommender import search_assessments

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def build_context(results):
    """Convert retrieved assessments into context for Gemini."""

    sections = []

    for item in results:
        sections.append(f"""
Assessment Name: {item.get("name")}

Description:
{item.get("description")}

Duration:
{item.get("duration")}

Job Levels:
{", ".join(item.get("job_levels", []))}

Languages:
{", ".join(item.get("languages", []))}

URL:
{item.get("link")}
""")

    return "\n\n-------------------------\n\n".join(sections)


def chat(user_query):
    results = search_assessments(user_query, top_k=10)

    context = build_context(results)

    prompt = f"""
{SYSTEM_PROMPT}

Relevant SHL Assessments

{context}

User Question:
{user_query}
"""

    # Try multiple models and retry on temporary server errors
    models = [
        "gemini-2.5-flash",
        "gemini-2.5-flash-lite",
        "gemini-2.0-flash",
    ]

    last_error = None

    for model_name in models:
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )
                return response.text

            except errors.ServerError:
                print(f"{model_name} is busy. Retrying...")
                time.sleep(3)
                last_error = None

            except Exception as e:
                last_error = e
                break

    raise RuntimeError(f"All Gemini models failed. Last error: {last_error}")


if __name__ == "__main__":
    while True:
        query = input("\nYou: ")

        if query.lower() == "exit":
            break

        print("\nAssistant:\n")
        print(chat(query))