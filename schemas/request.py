from pydantic import BaseModel, Field, model_validator
from typing import List, Optional

class BFHLRequest(BaseModel):
    fibonacci: Optional[int] = Field(default=None, ge=0)
    prime: Optional[List[int]] = None
    lcm: Optional[List[int]] = None
    hcf: Optional[List[int]] = None
    AI: Optional[str] = None

    @model_validator(mode="after")
    def check_exactly_one_field(self):
        values = [
            self.fibonacci,
            self.prime,
            self.lcm,
            self.hcf,
            self.AI
        ]
        if sum(v is not None for v in values) != 1:
            raise ValueError("Exactly one key must be provided")
        return self

    model_config = {
        "extra": "forbid"
    }
