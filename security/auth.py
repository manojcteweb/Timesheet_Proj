from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    # Implement token verification logic
    if token != "valid_token":
        raise HTTPException(status_code=403, detail="Invalid or expired token")