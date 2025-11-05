from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Union, Optional
from ..schemas.filters_sche import CategoriasProveedores
from ..schemas.providers_sche import ProveedorOut
from ..utils.extract_providers import obtener_todos_proveedores, obtener_proveedor_por_id
from fastapi_pagination import Page,paginate
router = APIRouter(
    prefix="/proveedores",
    tags=["proveedores"]
)




@router.get("", response_model=Page[ProveedorOut])
async def obtener_todos_los_proveedores(
    categoria: Union[CategoriasProveedores, None] = None,
    ubicacion: Optional[str] = None,
):
    """
    Obtiene todos los proveedores con filtros opcionales y paginación automática.
    
    La paginación se controla con los parámetros query:
    - **page**: Número de página (default: 1)
    - **size**: Tamaño de página (default: 50, max: 100)
    - **categoria**: Filtrar por categoría específica
    - **ubicacion**: Filtrar por ciudad

    """
    # Obtener todos los proveedores (esto debería ser tu lista o query)
    todos_proveedores = obtener_todos_proveedores()
    
    # Aplicar filtros
    proveedores_filtrados = todos_proveedores
    
    if categoria:
        proveedores_filtrados = [
            prov for prov in proveedores_filtrados 
            if prov.get("categoria", "").lower() == categoria.value.lower()
        ]
    
    if ubicacion:
        proveedores_filtrados = [
            prov for prov in proveedores_filtrados
            if prov.get("ubicacion", {}).get("ciudad", "").lower() == ubicacion.lower()
        ]

    
    return paginate(proveedores_filtrados)


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