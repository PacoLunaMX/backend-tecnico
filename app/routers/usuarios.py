from fastapi import  HTTPException, status, APIRouter
from app.models.user_model import UsuarioNew, UsuarioOut
from app.config.db import collection
from app.schemas.user_schema import users_serializer, user_serializer
from typing import List


router = APIRouter(
        prefix="/usuarios",
        tags=['Usuarios']
)

@router.post("/", response_model=UsuarioOut)
async def crear_usuario(usuario: UsuarioNew):

    nuevo_usuario = dict(usuario)
    hashed_password = hash(nuevo_usuario["password"])
    nuevo_usuario["password"] = hashed_password

    # revisar que el correo electrónico no esté registrado
    user_query = collection.find_one({"email":nuevo_usuario["email"]})
    if user_query:
         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Ya existe un usuario registrado con este correo.")

    _id = collection.insert_one(nuevo_usuario)
    user = collection.find_one({"_id": _id.inserted_id})
    return user



@router.get("/", response_model= List[UsuarioOut])
async def obtener_usuarios():
    users = users_serializer(collection.find())
    return users
            


@router.get("/{correo}", response_model=UsuarioOut)
async def obtener_usuario(correo: str):
   user_query = collection.find_one({"email":correo})

   if user_query is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El usuario con el correo: {correo} no fue encontrado")
   
   user = UsuarioOut(**user_query)
   
   return user


@router.delete("/{correo}", status_code=200)
async def eliminar_usuario(correo:str):
    query = { "email": correo}
    collection.delete_one(query)