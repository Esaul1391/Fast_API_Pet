from pydantic import BaseModel, EmailStr


#   схема для тела запроса
class SUserAuth(BaseModel):
    email: EmailStr
    password: str

