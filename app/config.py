from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # YouTube Music OAuth credentials
    ytmusic_client_id: str = ""
    ytmusic_client_secret: str = ""

    # Optional application settings
    app_name: str = "FastAPI Server"
    debug: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )


# Create a global settings instance
settings = Settings()
