from pydantic import BaseModel, EmailStr, constr, validator



class UsuarioBase(BaseModel):
    email: EmailStr
    phone: int
    first_name: constr(min_length=4, max_length=15) 
    last_name: constr(min_length=4, max_length=15) 

    @validator('phone')
    def phone_validator(cls, v):
        if (len(str(v))<10) | (len(str(v))>12):
            raise ValueError(f'El número de teléfono debe de ser un número válido de entre 10 y 12 dígitos. El número ingresado contiene {len(str(v))} dígitos')
        return v
    
    class Config:
        orm_mode = True

class UsuarioNew(UsuarioBase):
    password: str

class UsuarioOut(UsuarioBase):
    _id: str