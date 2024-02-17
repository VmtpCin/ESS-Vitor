from pydantic import BaseModel

# Model for user credentials
class Store(BaseModel):
    username: str
    cnpj: str
    email: str
    categoria: str
    password: str