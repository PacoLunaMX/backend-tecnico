from pydantic import BaseSettings


class Settings(BaseSettings):
   collection_name: str
   db_name: str
   db_username: str
   db_password: str

   class Config:
      env_file= ".env"

settings = Settings()