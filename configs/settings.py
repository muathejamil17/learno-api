from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    CONSUMER_KEY: str
    CONSUMER_SECRET: str
    DOMAIN: str
    DATA_BASE_URL: str
    ORGANIZATION_ID: int

    class Config:
        env_file = ".env"
