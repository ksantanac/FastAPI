from typing import Optional

from sqlmodel import Fieldm, SQLModel

class CursoModel(SQLModel, table=True):
    __tablename__ : str = 'cursos'
    
    id: Optional[int] = Field(default=None, primary_key= True)

