from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_name: str = "db"
    db_user: str = "user"
    db_password: str = "password"
    db_host: str = "localhost"
    db_port: int = 3306
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
