from databases import Database
from sqlalchemy import MetaData, create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./demo.db")
database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(str(DATABASE_URL).replace('asyncpg+',''), connect_args={"check_same_thread": False})
