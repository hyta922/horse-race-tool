import decimal
from typing import Optional
from pydantic import BaseModel, Field
from typing import List

class Activity(BaseModel):
    id: str
    user: str
    expired_date: decimal.Decimal
    note: Optional[str] = None