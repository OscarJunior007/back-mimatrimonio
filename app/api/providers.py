from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Union, Optional
from ..schemas.filters_sche import CategoriasProveedores
from ..utils.extract_providers import obtener_todos_proveedores, obtener_proveedor_por_id

router = APIRouter(
    prefix="/proveedores",
    tags=["proveedores"]
)

@router.get("")
async def obtener_todos_los_proveedores(
    categoria: Union[CategoriasProveedores, None] = None,
    ubicacion: Optional[str] = None,
    precio_max: Optional[int] = None,
    limite: Optional[int] = 100
):
    """
    Obtiene todos los proveedores con filtros opcionales
    
    - **categoria**: Filtrar por categoría específica
    - **ubicacion**: Filtrar por ciudad
    - **precio_max**: Precio máximo inicial
    - **limite**: Número máximo de resultados
    """
    todos_proveedores = obtener_todos_proveedores()
    
    # Aplicar filtro de categoría
    if categoria:
        todos_proveedores = [
            prov for prov in todos_proveedores 
            if prov.get("categoria", "").lower() == categoria.value.lower()
        ]
    
    # Aplicar filtro de ubicación
    if ubicacion:
        todos_proveedores = [
            prov for prov in todos_proveedores
            if prov.get("ubicacion", {}).get("ciudad", "").lower() == ubicacion.lower()
        ]
    
    # Aplicar filtro de precio
    if precio_max:
        todos_proveedores = [
            prov for prov in todos_proveedores
            if prov.get("precio", {}).get("precio_inicial", float('inf')) <= precio_max
        ]
    
    # Limitar resultados
    if limite:
        todos_proveedores = todos_proveedores[:limite]
    
    return {
        "success": True,
        "data": {
            "proveedores": todos_proveedores,
            "total": len(todos_proveedores)
        }
    }


@router.get("/{proveedor_id}")
async def obtener_proveedor_por_id_endpoint(proveedor_id: str):
    """
    Obtiene un proveedor específico por su ID
    
    - **proveedor_id**: ID único del proveedor (ej: wp-bog-001, fot-bar-001)
    """
    proveedor = obtener_proveedor_por_id(proveedor_id)
    
    if not proveedor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Proveedor con ID '{proveedor_id}' no encontrado"
        )
    
    return {
        "success": True,
        "data": {
            "proveedor": proveedor
        }
    }