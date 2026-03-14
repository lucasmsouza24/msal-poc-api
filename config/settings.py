from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    msal_client_id: str
    msal_client_secret: str
    msal_authority: str
    redirect_uri: str
    frontend_uri: str
    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_password: str

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
