from typing import List, Optional, Any

from fastapi.responses import JSONResponse
from fastapi import Header
from fastapi import Query
from fastapi import Path
from fastapi import Response

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends

from time import sleep

from models import Curso

def fake_db():
    try:
        print("Abrindo conexao com o banco de dados")
        sleep(1)
    
    finally:
        print("Fechando conexão com banco de dados")
        sleep(1)


app = FastAPI()

cursos = {
    1: {
        "titulo": "Python para Iniciantes",
        "aulas": 112,
        "horas": 58,
    },
    2: {
        "titulo": "Algoritmos e lógica de Progamação",
        "aulas": 87,
        "horas": 67,
    },
}

# Retornar todos os cursos
@app.get("/cursos")
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

# Retornar curso por id
@app.get("/cursos/{curso_id}")
async def get_curso(curso_id : int = Path(default=None, title="ID do curso", description="Entre 1 e 2", ge=1, lt=3), db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=404, detail='Curso não encontrado.')

# Adicionando um curso
@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

# Atualizando curso
@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Não existe um curso com id {curso_id}")
        
# Deletando um curso
@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        
        return Response(status_code=status.HTTP_204_NO_CONTENT)
        
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Curso com id {curso_id} não existe")
    

# Uso do Query Parameters / Headers Parameters
@app.get("/calculadora")
async def calcular(
    a: int = Query(default=None, ge=5), b: int = Query(default=None, le=10), 
    x_geek: str = Header(default=None), c: Optional[int] = None
    ):
    soma: int = a + b
    if c:
        soma = soma + c
    
    # Headers Parameteres
    print(f"X-GEEK: {x_geek}")

    return {"Resultado": soma}





if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, debug=True, reload=True)