from pydantic import BaseModel
from datetime import datetime


class MesureTemporelle(BaseModel):
    d: datetime
    v: float
