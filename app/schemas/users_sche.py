from pydantic import BaseModel,EmailStr,Field,field_validator
from typing import Optional, List,Dict
import uuid
from fastapi import status
class UsuarioRegistroEmpresa(BaseModel):
    email: EmailStr
    password: str
    nombre_empresa: str
    tipo_empresa_id: str
    tipo_proveedor_id: Optional[str] = None
    id_ciudad: Optional[str] = None
    
   
    usuario_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    empresa_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    perfil_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    
    @field_validator('password')
    def validar_password(cls, v):
        if len(v) < 8 or len(v) > 48:
            raise ValueError('La contraseña debe tener entre 8 y 48 caracteres')
        
        tiene_mayuscula = any(c.isupper() for c in v)
        tiene_minuscula = any(c.islower() for c in v)
        tiene_numero = any(c.isdigit() for c in v)
        tiene_espacio = ' ' in v
        
        if not tiene_mayuscula:
            raise ValueError('La contraseña debe contener al menos una letra mayúscula')
        if not tiene_minuscula:
            raise ValueError('La contraseña debe contener al menos una letra minúscula')
        if not tiene_numero:
            raise ValueError('La contraseña debe contener al menos un número')
        if tiene_espacio:
            raise ValueError('La contraseña no puede contener espacios')
        
        return v
    
class UsuarioRegistroPareja(BaseModel):
    email: EmailStr
    password: str
    nombre_completo: str
    whatsapp: str
    id_ciudad: str
    
    # IDs generados automáticamente
    usuario_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    pareja_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    perfil_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    
    @field_validator('password')
    def validar_password(cls, v):
        if len(v) < 8 or len(v) > 48:
            raise ValueError('La contraseña debe tener entre 8 y 48 caracteres')
        
        tiene_mayuscula = any(c.isupper() for c in v)
        tiene_minuscula = any(c.islower() for c in v)
        tiene_numero = any(c.isdigit() for c in v)
        tiene_espacio = ' ' in v
        
        if not tiene_mayuscula:
            raise ValueError('La contraseña debe contener al menos una letra mayúscula')
        if not tiene_minuscula:
            raise ValueError('La contraseña debe contener al menos una letra minúscula')
        if not tiene_numero:
            raise ValueError('La contraseña debe contener al menos un número')
        if tiene_espacio:
            raise ValueError('La contraseña no puede contener espacios')
        
        return v
    
class UsuarioRegistroEmpresa(BaseModel):
    usuario_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    empresa_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    perfil_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr = Field(...)
    password: str = Field(...)
    nombre_empresa: str = Field(...)
    tipo_empresa_id: str = Field(...)
    categoria_empresa_id: str = Field(...) #si tipo_empresa =  proveedor entonces = (fotografia,catering etc) ----- si   tipo_empresa = recepcion entonces = (finca,hotel,etc) 
    id_ciudad: str = Field(...)
    
class UsuarioEmpresaResponse(BaseModel):
    usuario_id: uuid.UUID | None
    email: str
    mensaje: str
    exito: bool
    status_code: int 
