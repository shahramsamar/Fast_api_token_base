from pydantic import BaseModel

    
class LoginResponseSchema(BaseModel):
    token: str
    user_id: int
    detail: str


class LoginRequestSchema(BaseModel):
    email: str
    password: str
