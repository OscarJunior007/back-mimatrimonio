from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import json
from datetime import datetime
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from enum  import Enum
from typing import Union
from app.api import providers
from fastapi_pagination import Page, add_pagination, paginate


def include_router(app):
    app.include_router(providers.router)  
    # app.include_router(users.router)
    # app.include_router(places.router)


def start_application():
    app = FastAPI(
    title="API Matrimonio.com.co",
    description="API para plataforma de bodas - Directorio de proveedores",
    version="1.0.0"
)
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","https://mi-matrimonio-web.web.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    add_pagination(app)
    include_router(app)
    return app  

app = start_application()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)