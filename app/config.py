from pydantic import root_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


#   переделать
class Settings(BaseSettings):
    # DB_HOST: str
    # DB_PORT: int
    # DB_USER: str
    # DB_PASS: str
    # DB_NAME: str   обязательно найти ошибку

    @property
    def DATABASE_URL(self):
        # return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql+asyncpg://postgres:1111@localhost:5432/postgres"

    # Со 2 версии Pydantic, class Config был заменен на атрибут model_config
    # class Config:
    #     env_file = ".env"
    # model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
