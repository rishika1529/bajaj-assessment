
from fastapi import APIRouter, HTTPException
from ..main import (
    BFHLRequest,
    fibonacci_series,
    filter_primes,
    compute_lcm,
    compute_hcf,
    ask_gemini,
    OFFICIAL_EMAIL,
)

router = APIRouter()

@router.post("/bfhl")
def bfhl(req: BFHLRequest):
    try:
        if req.fibonacci is not None:
            data = fibonacci_series(req.fibonacci)

        elif req.prime is not None:
            if not req.prime:
                raise ValueError("Array cannot be empty.")
            data = filter_primes(req.prime)

        elif req.lcm is not None:
            if not req.lcm:
                raise ValueError("Array cannot be empty.")
            data = compute_lcm(req.lcm)

        elif req.hcf is not None:
            if not req.hcf:
                raise ValueError("Array cannot be empty.")
            data = compute_hcf(req.hcf)

        elif req.AI is not None:
            data = ask_gemini(req.AI)

        else:
            raise ValueError("Invalid request")

        return {
            "is_success": True,
            "official_email": OFFICIAL_EMAIL,
            "data": data
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
