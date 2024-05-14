from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def db_url(self) -> str:
        return (
            f"mysql+aiomysql://"
            f"{self.db_host}:{self.db_port}/{self.db_name}?"
            f"user={self.db_user}&"
            f"password={self.db_password}"
        )


settings = Settings()
