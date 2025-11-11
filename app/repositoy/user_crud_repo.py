import asyncpg
from typing import Dict, Any
import uuid
from app.utils.jwt import get_password_hash
from app.schemas.users_sche import UsuarioRegistroEmpresa
from app.schemas.empresas_sche import CategoriaEmpresaResponse,CiudadesResponse
from typing import List
async def registrar_usuario_pareja(
    conn: asyncpg.Connection,
    usuario_id: str,
    pareja_id: str,
    perfil_id: str,
    email: str,
    password: str,
    nombre_completo: str,
    whatsapp: str,
    id_ciudad: str
) -> Dict[str, Any]:
    """
    Registra un nuevo usuario de tipo Pareja usando la función de PostgreSQL.
    Hashea la contraseña antes de enviarla a la base de datos.
    """
  
    password_hash = get_password_hash(password)
    

    query = """
        SELECT * FROM registrar_usuario_pareja(
            $1::UUID, $2::UUID, $3::UUID, $4::TEXT, $5::TEXT, 
            $6::TEXT, $7::TEXT, $8::UUID
        )
    """
    
    row = await conn.fetchrow(
        query,
        uuid.UUID(usuario_id),
        uuid.UUID(pareja_id),
        uuid.UUID(perfil_id),
        email,
        password_hash,
        nombre_completo,
        whatsapp,
        uuid.UUID(id_ciudad)
    )
    
    return dict(row)

async def get_all_categorias_empresas(conn: asyncpg.Connection,) -> List[CategoriaEmpresaResponse]:
    """
    Retorna todas las categorías de empresas con su tipo de empresa asociado.
    """
    query = """
        SELECT * FROM obtener_todas_categorias();

    """

    rows = await conn.fetch(query)
    return [CategoriaEmpresaResponse(**dict(row)) for row in rows]

async def get_all_ciudades(conn:asyncpg.connection) -> List[CiudadesResponse]:
    
    query = """
        SELECT * FROM obtener_todos_departamento_ciudades();
    """
    rows = await conn.fetch(query)
    return[CiudadesResponse(**dict(row)) for row in rows]


async def registrar_usuario_empresa(
    conn: asyncpg.Connection,
    dataUser: UsuarioRegistroEmpresa
) -> Dict[str, Any]:
    """
    Registra un nuevo usuario de tipo Empresa usando la función de PostgreSQL.
    Hashea la contraseña antes de enviarla a la base de datos.
    """
    # Hashear la contraseña
    password_hash = get_password_hash(dataUser.password)

    
    
    query = """
        SELECT * FROM registrar_usuario_empresa(
            $1::UUID, $2::UUID, $3::UUID, $4::TEXT, $5::TEXT,
            $6::TEXT, $7::UUID, $8::UUID, $9::UUID
        )
    """
    
    print("data que llego del usuario: ",dataUser)
    
    row = await conn.fetchrow(
        query,
        dataUser.usuario_id,
        dataUser.empresa_id,
        dataUser.perfil_id,
        dataUser.email,
        password_hash,
        dataUser.nombre_empresa,
        dataUser.tipo_empresa_id,
        dataUser.categoria_empresa_id,
        dataUser.id_ciudad
    )
    
    return dict(row)