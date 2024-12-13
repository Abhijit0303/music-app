from pydantic import BaseModel


class UserLogin(BaseModel):
    """User Login Model"""

    email: str
    password: str