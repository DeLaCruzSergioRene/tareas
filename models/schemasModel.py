from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time

class UsuarioSchema(BaseModel):
    nombre: str = Field(min_length=3, max_lenght=100)
    email: EmailStr
    password: str = Field(min_lenght=8)
    
class TareaSchema(BaseModel):
    titulo: str = Field(min_lenght=1, max_lenght=200)
    descripcion: Optional[str] = None
    prioridad: str = "media"
    clasificacion: str = "personal"