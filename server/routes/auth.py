import uuid
import bcrypt
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from pydantic_schema.user_create import UserCreate
from pydantic_schema.user_login import UserLogin


router = APIRouter()

@router.post('/signup', status_code=201)
def signup_user(user: UserCreate, db: Session=Depends(get_db)):
    """This is the signup api woriking"""

    #Check if the User already exits
    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(400, 'User with same email already exists')

    #If not exists then it should create a user
    hashed_pwd = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()), name=user.name, email=user.email, password=hashed_pwd)

    #Add the user in the database
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db


@router.post('/login')
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    """API of login user working"""

    #Check if the user with same email exists
    user_db = db.query(User).filter(User.email == user.email).first()

    if not user_db:
        raise HTTPException(400, 'User with this email does not exist')

    #Check if the password matching or not
    is_match = bcrypt.checkpw(user.password.encode(), user_db.password)

    if not is_match:
        raise HTTPException(400, 'Incorrect password')

    #if everything correct then should return the data
    return user_db
