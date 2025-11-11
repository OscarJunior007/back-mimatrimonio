
from ..schemas.empresas_sche import CategoriaEmpresaResponse

from fastapi import APIRouter, HTTPException, status,Depends
from fastapi.responses import JSONResponse
from typing import Union, Optional

import asyncpg
from app.repositoy.database import get_db
from app.repositoy.user_crud_repo import get_all_categorias_empresas,get_all_ciudades

router = APIRouter(
    prefix="/api/empresa",
    tags=["empresas"]
)


@router.get("/categoria")
async def obtener_categorias(db: asyncpg.Connection = Depends(get_db)):
    try:
        resultado =  await get_all_categorias_empresas(db)
        return resultado
        
    except Exception as e:
        print("error:",e)
        
@router.get("/ciudades")
async def obtener_ciudades(db: asyncpg.Connection = Depends(get_db)):
    try:
        resultado =  await get_all_ciudades(db)
        # print(resultado)
        return resultado
    except Exception as e:
        print("error:",e)
