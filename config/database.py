import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import connection
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class ConfiguracoesPostgres(BaseSettings):
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"  # noqa: S105
    POSTGRES_DB: str = "bancorn"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def dsn(self) -> str:
        return (
            f"dbname={self.POSTGRES_DB} "
            f"user={self.POSTGRES_USER} "
            f"password={self.POSTGRES_PASSWORD} "
            f"host={self.POSTGRES_HOST} "
            f"port={self.POSTGRES_PORT}"
        )

    def sqlalchemy_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


configuracoes_postgres = ConfiguracoesPostgres()


def obter_conexao_banco() -> connection:
    return psycopg2.connect(configuracoes_postgres.dsn)
