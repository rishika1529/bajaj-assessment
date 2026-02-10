from fastapi import APIRouter, HTTPException, status

from schemas.response import SuccessResponse
from schemas.request import BFHLRequest
from services.logic import (
    fibonacci_series,
    filter_primes,
    find_hcf,
    find_lcm
)
from app.config import EMAIL
from services.llm import ask_ai
router = APIRouter(tags=["BFHL"])


@router.get(
    "/health",
    response_model=SuccessResponse,
    status_code=status.HTTP_200_OK
)
def health_check():
    return {
        "is_success": True,
        "official_email": EMAIL
    }


@router.post(
    "/bfhl",
    response_model=SuccessResponse,
    status_code=status.HTTP_200_OK
)
def bfhl_handler(payload: BFHLRequest):

    try:
        if payload.fibonacci is not None:
            data = fibonacci_series(payload.fibonacci)

        elif payload.prime is not None:
            data = filter_primes(payload.prime)

        elif payload.lcm is not None:
            data = find_lcm(payload.lcm)

        elif payload.hcf is not None:
            data = find_hcf(payload.hcf)

        elif payload.AI is not None:
            data = ask_ai(payload.AI)

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Exactly one key is required"
            )

        return {
            "is_success": True,
            "official_email": EMAIL,
            "data": data
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )


