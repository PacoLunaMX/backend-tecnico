from pymongo import MongoClient
from app.config.config import settings


client = MongoClient(f"mongodb+srv://{settings.db_username}:{settings.db_password}@testing.nli0tbu.mongodb.net/?retryWrites=true&w=majority")

try:
    db = client[settings.db_name]
    collection = db[settings.collection_name]
    # Create new index
    collection.create_index('email', unique=True)
except AttributeError as error:
    print("Hubo un ERROR al obtener la base de datos y la colección de Mongo DB", error)
