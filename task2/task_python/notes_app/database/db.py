from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
import os


load_dotenv()

url = URL.create(
    drivername="postgresql",
    username=os.getenv("DB_USERNAME"),
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

engine = create_engine(url)

if not database_exists(engine.url):    
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

os.environ["DB_URL"] = str(url)




