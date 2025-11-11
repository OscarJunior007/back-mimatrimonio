# from fastapi import Depends, HTTPException, status, Request
# from fastapi.security import OAuth2PasswordBearer
# from app.utils.jwt import decode_token, verify_password   


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/users/login")



# async def authenticate_user_google(email: str): 
#     try:
#         user = await get_user_by_email(email)  
#         if not user:
#             raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
#         return user
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error de autenticación: {str(e)}")


# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     """
#     Extrae y valida el token del header Authorization: Bearer <token>
#     """
#     try:
#         payload = decode_token(token)
#         email = payload.get("email")
        
#         if email is None:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Token inválido"
#             )
        
#         if len(payload) == 2:
#             user = await get_user_by_email(email)
#             return UserOut(**user)
        
#         return UserOut(**payload)
        
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail=f"No se pudo validar el token: {str(e)}"
#         )


# async def check_permission(current_user, required_permission: str):
#     permissions = await get_user_permissions(current_user.email)
#     if required_permission not in permissions:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="No tienes permisos para esta acción"
#         )


# def PermissionDependency(required_permission: str):
#     async def wrapper(current_user=Depends(get_current_user)):
#         await check_permission(current_user, required_permission)
#         return current_user
#     return wrapper