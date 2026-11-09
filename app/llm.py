import os

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from app.schemas import RequirementExtraction
from app.prompts import EXTRACTION_PROMPT

load_dotenv(find_dotenv())

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("La variable OPENAI_API_KEY n'est pas définie. Ajoute-la dans ton fichier .env.")

client = OpenAI(api_key=api_key)


def get_completion(prompt: str, model: str = "gpt-4o-mini") ->RequirementExtraction:
    response = client.chat.completions.parse(
        response_format=RequirementExtraction,
        model=model,
        messages=[{"role":"system","content": EXTRACTION_PROMPT},{"role": "user", "content": prompt},],
        temperature=0,
    )
    return response.choices[0].message.parsed