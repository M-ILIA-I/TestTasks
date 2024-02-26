from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import os
from sqlalchemy.orm import sessionmaker


load_dotenv()

url = f'postgresql+asyncpg://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'

engine = create_async_engine(url)

# if not database_exists(engine.url):    
#     create_database(engine.url)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

os.environ["DB_URL"] = str(url)




