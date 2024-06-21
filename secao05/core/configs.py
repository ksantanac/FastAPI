# from pydantic.settings import BaseSettings
from pydantic_settings import BaseSettings


# Definição da classe de configurações usando Pydantic
class Settings(BaseSettings):
    # Prefixo da versão da API
    API_V1_STR: str = 'api/v1'
    
    # URL de conexão com o banco de dados PostgreSQL usando asyncpg
    DB_URL: str = "postgresql+asyncpg://postgres:rekaue13@localhost:5432/faculdade"
    
    # Classe interna para configurações adicionais
    class Config:
        # Sensibilidade a maiúsculas/minúsculas para variáveis de ambiente
        case_sensitive = True
        
# Instanciação do objeto de configurações
settings: Settings = Settings()
