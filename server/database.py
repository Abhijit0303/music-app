import os
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


DATABASE_URL = URL.create(
    drivername=os.getenv('DB_DRIVERNAME'),
    username=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    database=os.getenv('DB_DATABASE_NAME'),
    port=os.getenv('DB_PORT')
)

engine = create_engine(url=DATABASE_URL)
SessioLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

def get_db():
    db = SessioLocal()
    try:
        yield db
    finally:
        db.close()
