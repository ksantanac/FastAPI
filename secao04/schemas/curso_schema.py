from typing import Optional

from pydantic import BaseModel as SCBaseModel

class CursoSchema(SCBaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horras: int
    
    class Config:
        orm_mode = True