from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os


load_dotenv()

url = URL.create(
    drivername="postgresql",
    username=os.getenv("DB_USERNAME"),
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME")
)

engine = create_engine(url)


