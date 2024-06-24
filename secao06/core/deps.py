from typing import Generator  # Importa a classe Generator para especificar o tipo de retorno da função

from sqlalchemy.ext.asyncio import AsyncSession  # Importa a classe AsyncSession para sessões assíncronas com SQLAlchemy

from core.database import Session  # Importa o objeto Session, que é configurado para criar sessões de banco de dados

# Define uma função assíncrona chamada get_session que retorna um Generator
async def get_session() -> Generator:
    # Cria uma nova sessão assíncrona do SQLAlchemy
    session: AsyncSession = Session()
    
    try:
        # O bloco try é usado para garantir que a sessão seja fechada corretamente
        yield session  # Yield retorna a sessão para ser usada no contexto atual (por exemplo, dentro de uma rota FastAPI)
    finally:
        # O bloco finally é sempre executado, garantindo que a sessão seja fechada mesmo se ocorrer uma exceção
        await session.close()  # Fecha a sessão assíncrona
