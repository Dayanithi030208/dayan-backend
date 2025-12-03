from datetime import datetime, timedelta
from jose import jwt
from app.core.config import settings
from fastapi import HTTPException, Depends
from jose import jwt, JWTError
from app.core.config import settings
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

def verify_token_and_get_user(creds: HTTPAuthorizationCredentials = Depends(security)):
    token = creds.credentials
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        return int(user_id)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=6)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
