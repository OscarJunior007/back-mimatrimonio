from pydantic import BaseModel
from typing import Optional,List, Dict
from enum import  Enum

class CategoriasProveedores(Enum):
    FOTOGRAFIA = "fotografia"
    WEDDING_PLANNER = "wedding planner"