from pydantic import BaseModel
class NamesSchema(BaseModel):
    name : str 

    
class ResponseNamesSchema(NamesSchema):
    id: int


class RegisterUserSchema(BaseModel):
    email: str
    password: str
    user: str  # Should be "user" or "admin"
