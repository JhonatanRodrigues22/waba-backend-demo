from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str = "development"
    app_name: str = "WABA Backend Demo"

    host: str = "0.0.0.0"
    port: int = 8000

    waba_verify_token: str | None = None
    waba_access_token: str | None = None
    waba_phone_number_id: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
