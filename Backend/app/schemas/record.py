from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class RecordCreate(BaseModel):
    amount: float = Field(..., gt=0)
    type: Literal["income", "expense"]
    category: str = Field(..., min_length=2)
    date: datetime
    notes: Optional[str] = None


class RecordResponse(BaseModel):
    amount: float
    type: str
    category: str
    date: datetime
    notes: Optional[str]