from pydantic import BaseModel
from typing import Any, Optional

class SuccessResponse(BaseModel):
    is_success: bool
    official_email: str
    data: Optional[Any] = None
