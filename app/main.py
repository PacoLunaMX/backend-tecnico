from fastapi import FastAPI
from app.routers import usuarios
from dotenv import dotenv_values
from pymongo import MongoClient


app = FastAPI()

@app.get("/")
def root():
    return { "mensaje" : "Bienvenido"}


app.include_router(router = usuarios.router)


