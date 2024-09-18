from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    CONSUMER_KEY: str
    CONSUMER_SECRET: str
    DOMAIN: str
    QUESTIONS_ENDPOINT: str
    ORGANIZATION_ID: int

    class Config:
        env_file = ".env"
