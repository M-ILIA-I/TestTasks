from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL


url = URL.create(
    drivername="postgresql",
    username="ilya",
    host="localhost",
    database="test_db"
)

engine = create_engine(url)

