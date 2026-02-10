import os
import math
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, root_validator
import requests

app = FastAPI(title="BFHL API")

OFFICIAL_EMAIL = os.getenv(
    "OFFICIAL_EMAIL",
    "rishika2193.be23@chitkara.edu.in"
)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ---------- Utility Functions ----------

def fibonacci_series(n: int) -> List[int]:
    if n < 0:
        raise ValueError("Fibonacci input must be non-negative.")
    if n == 0:
        return []
    if n == 1:
        return [0]

    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series


def filter_primes(arr: List[int]) -> List[int]:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    return [x for x in arr if is_prime(x)]


def compute_lcm(arr: List[int]) -> int:
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    result = arr[0]
    for num in arr[1:]:
        result = lcm(result, num)
    return result


def compute_hcf(arr: List[int]) -> int:
    result = arr[0]
    for num in arr[1:]:
        result = math.gcd(result, num)
    return result


# ---------- Gemini AI ----------

def ask_gemini(question: str) -> str:
    if not GEMINI_API_KEY:
        return "AI_KEY_NOT_CONFIGURED"

    url = (
        "https://generativelanguage.googleapis.com/v1beta/"
        f"models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f"Answer in one word only: {question}"}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, json=payload, timeout=10)

        if response.status_code != 200:
            return "AI_ERROR"

        data = response.json()

        text = data["candidates"][0]["content"]["parts"][0]["text"]
        return text.strip().split()[0]

    except Exception:
        return "UNKNOWN"


# ---------- Request Schema ----------

class BFHLRequest(BaseModel):
    fibonacci: int | None = None
    prime: List[int] | None = None
    lcm: List[int] | None = None
    hcf: List[int] | None = None
    AI: str | None = None

    @root_validator(pre=True)
    def validate_single_key(cls, values):
        provided = [k for k, v in values.items() if v is not None]
        if len(provided) != 1:
            raise ValueError("Exactly one key must be provided.")
        return values


# ---------- Routers ----------

from .routers import bfhl, health

app.include_router(bfhl.router)
app.include_router(health.router)
