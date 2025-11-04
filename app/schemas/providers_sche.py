from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


class Ubicacion(BaseModel):
    ciudad: str
    departamento: str
    direccion: str


class RedesSociales(BaseModel):
    facebook: Optional[str] = None
    instagram: Optional[str] = None


class Contacto(BaseModel):
    telefono: str
    email: str
    sitio_web: str
    redes_sociales: Optional[RedesSociales] = None


class Calificacion(BaseModel):
    puntuacion: float
    num_opiniones: int
    porcentaje_recomendacion: Optional[float] = None


class Precio(BaseModel):
    precio_inicial: int
    precio_maximo: Optional[int] = None
    rango_precio: Optional[str] = None


class ProveedorOut(BaseModel):
    id: str
    nombre: str
    categoria: str
    ubicacion: Ubicacion
    contacto: Contacto
    calificacion: Calificacion
    precio: Precio
    servicios: Optional[List[str]] = None
    imagen_principal: Optional[str] = None
    
    class Config:
        from_attributes = True



class ProveedoresResponse(BaseModel):
    success: bool
    data: dict
    
    class Config:
        from_attributes = True


class CategoriasProveedores(str, Enum):
    WEDDING_PLANNER = "Wedding Planner"
    FOTOGRAFIA = "Fotografia"
    VIDEO = "Video"
    CATERING = "Catering"
    MUSICA = "Musica"
    FLORES = "Flores"
    DECORACION = "Decoracion"
    MOBILIARIO = "Mobiliario"
    # Agrega más categorías según necesites