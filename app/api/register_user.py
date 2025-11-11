
from ..schemas.users_sche import UsuarioRegistroEmpresa,UsuarioEmpresaResponse

from fastapi import APIRouter, HTTPException, status,Depends
from fastapi.responses import JSONResponse
from typing import Union, Optional
from ..schemas.filters_sche import CategoriasProveedores
from ..schemas.providers_sche import ProveedorOut

from ..utils.extract_providers import obtener_todos_proveedores, obtener_proveedor_por_id
from fastapi_pagination import Page,paginate

import asyncpg
from app.repositoy.database import get_db
from app.repositoy.user_crud_repo import registrar_usuario_empresa

router = APIRouter(
    prefix="/api/user",
    tags=["user"]
)

@router.post("/emp",response_model=UsuarioEmpresaResponse)
async def register_user_empresa(datos:UsuarioRegistroEmpresa,db: asyncpg.Connection = Depends(get_db)):
    try:
        resultado = await registrar_usuario_empresa(db, datos)

        if not resultado["exito"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=resultado["mensaje"]
            )

        return UsuarioEmpresaResponse(
        usuario_id=resultado["usuario_id"],
        email=resultado["email"],
        mensaje=resultado["mensaje"],
        exito=resultado["exito"],
        status_code=status.HTTP_201_CREATED
    )

    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {str(e)}"
        )
        

