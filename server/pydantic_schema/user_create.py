from pydantic import BaseModel


class UserCreate(BaseModel):
    """User creation Model"""
    name: str
    email: str
    password: str
