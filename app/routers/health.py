
from fastapi import APIRouter
from ..main import OFFICIAL_EMAIL

router = APIRouter()

@router.get("/health")
def health():
    return {
        "is_success": True,
        "official_email": OFFICIAL_EMAIL
    }
