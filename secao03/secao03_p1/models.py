from typing import Optional

from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int # + de 12 aulas
    horas: int # + de 10 horas
    
    @validator("titulo")
    def validar_titulo(cls, value: str):
        # Validaçaõ 1
        palavras = value.split(" ")
        if len(palavras) < 3:
            raise ValueError("O título deve ter pelo menos 3 palavras")
        
        # Validaçaõ 2
        if value.islower():
            raise ValueError("O titulo deve ser capitalizado")
    
        
        return value
    
    @validator("aulas")
    def validar_aula(cls, value: int):
        if value < 12:
            raise ValueError("O curso deve ter pelo menos 12 aulas")
        
        return value
    
    @validator("horas")
    def validar_hora(cls, value: int):
        if value < 10:
            raise ValueError("O curso deve ter pelo menos 10 horas")
        
        return value
    
cursos = [
    Curso(id=1, titulo="Programação para iniciantes", aulas=42, horas=56),
    Curso(id=2, titulo="Algoritmos e lógica de Programação", aulas=52, horas=66)
]