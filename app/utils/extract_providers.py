import json
import os
from typing import List, Dict, Optional

# Ruta al archivo JSON de proveedores
PROVIDERS_JSON_PATH = os.path.join(
    os.path.dirname(__file__), 
    "data", 
    "proveedores.json"
)

def cargar_proveedores_json() -> Dict:
    """
    Carga el archivo JSON de proveedores
    """
    try:
        with open(PROVIDERS_JSON_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"❌ Archivo no encontrado: {PROVIDERS_JSON_PATH}")
        return {}
    except json.JSONDecodeError as e:
        print(f"❌ Error al decodificar JSON: {e}")
        return {}


def obtener_todos_proveedores() -> List[Dict]:
    """
    Obtiene todos los proveedores del JSON en una lista plana
    
    La estructura original es:
    {
        "Categoria": {
            "Ciudad": [
                { proveedor1 },
                { proveedor2 }
            ]
        }
    }
    
    Se convierte en una lista plana de proveedores
    """
    data = cargar_proveedores_json()
    proveedores = []
    
    # Iterar por cada categoría
    for categoria, ciudades in data.items():
        # Iterar por cada ciudad dentro de la categoría
        for ciudad, lista_proveedores in ciudades.items():
            # Agregar cada proveedor a la lista
            if isinstance(lista_proveedores, list):
                proveedores.extend(lista_proveedores)
    
    return proveedores


def obtener_proveedor_por_id(proveedor_id: str) -> Optional[Dict]:
    """
    Busca un proveedor específico por su ID
    
    Args:
        proveedor_id: ID del proveedor (ej: wp-bog-001, fot-bar-001)
    
    Returns:
        Dict con los datos del proveedor o None si no se encuentra
    """
    todos_proveedores = obtener_todos_proveedores()
    
    for proveedor in todos_proveedores:
        if proveedor.get("id") == proveedor_id:
            return proveedor
    
    return None


def obtener_proveedores_por_categoria(categoria: str) -> List[Dict]:
    """
    Obtiene todos los proveedores de una categoría específica
    """
    data = cargar_proveedores_json()
    proveedores = []
    
    # Buscar la categoría (case insensitive)
    for cat_name, ciudades in data.items():
        if cat_name.lower() == categoria.lower():
            for ciudad, lista_proveedores in ciudades.items():
                if isinstance(lista_proveedores, list):
                    proveedores.extend(lista_proveedores)
            break
    
    return proveedores


def obtener_proveedores_por_ciudad(ciudad: str) -> List[Dict]:
    """
    Obtiene todos los proveedores de una ciudad específica
    """
    data = cargar_proveedores_json()
    proveedores = []
    
    # Buscar en todas las categorías
    for categoria, ciudades in data.items():
        for ciudad_name, lista_proveedores in ciudades.items():
            if ciudad_name.lower() == ciudad.lower():
                if isinstance(lista_proveedores, list):
                    proveedores.extend(lista_proveedores)
    
    return proveedores


def obtener_categorias_disponibles() -> List[str]:
    """
    Obtiene la lista de categorías disponibles
    """
    data = cargar_proveedores_json()
    return list(data.keys())


def obtener_ciudades_disponibles() -> List[str]:
    """
    Obtiene la lista de ciudades disponibles
    """
    data = cargar_proveedores_json()
    ciudades = set()
    
    for categoria, ciudades_dict in data.items():
        ciudades.update(ciudades_dict.keys())
    
    return sorted(list(ciudades))