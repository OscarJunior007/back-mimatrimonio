from jose import jwt    
from jose.exceptions import JWTError
from datetime import datetime,timedelta,timezone
import bcrypt
from dotenv import load_dotenv
import os

load_dotenv()
  
secret_key = os.getenv("SECRET_KEY")  
algorithm = os.getenv("ALGORITHM", "HS256")  

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy() 
    expire =  datetime.now(timezone.utc) + expires_delta if expires_delta else datetime.now(timezone.utc) + timedelta(minutes=60)   
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode,secret_key,algorithm=algorithm)

def decode_token(token:str):
    try:
        return jwt.decode(token,secret_key,algorithms=[algorithm])  
    except JWTError as e: 
        return {"error":str(e)} 
    
    
def get_password_hash(password:str) ->str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)     
    return hashed_password.decode('utf-8')


def verify_password(password:str, hash_password:str) -> str:
    return bcrypt.checkpw(password.encode('utf-8'), hash_password.encode('utf-8'))  