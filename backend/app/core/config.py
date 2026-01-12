from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    APP_ENV: str = "development"
    APP_NAME: str = "WABA Backend Demo"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    LOG_LEVEL: str = "INFO"

    # WABA / Meta
    WABA_VERIFY_TOKEN: str = "dev_verify_token"


settings = Settings()
