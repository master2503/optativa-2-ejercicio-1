from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "pendiente"  # columnas: pendiente, en_progreso, completada
