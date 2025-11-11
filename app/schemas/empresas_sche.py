from pydantic import BaseModel,EmailStr,Field,field_validator
from typing import Optional, List,Dict
import uuid
from fastapi import status

class CategoriaEmpresaResponse(BaseModel):
    id: uuid.UUID
    nombre: str
    descripcion: str | None
    icono: str | None
    activo: bool
    orden: int | None
    tipo_empresa_id: uuid.UUID
    tipo_empresa_nombre: str
    tipo_emp_id:uuid.UUID

class CiudadesResponse(BaseModel):
    id_ciudad: uuid.UUID
    nombre_ciudad:str
    nombre_departamento:str
    id_departamento:uuid.UUID
    nombre_pais:str