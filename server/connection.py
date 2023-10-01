import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL


url_object = URL.create(
    "postgresql+psycopg2",
    username=os.getenv("DATABASE_USERNAME"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    database=os.getenv("DATABASE_NAME"),
)

def get_engine():
    engine = create_engine(url_object)
    return engine
