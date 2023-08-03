import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

# DATABASE_CLIENT = os.getenv("DATABASE_CLIENT")
# DATABASE_HOST = os.getenv("DATABASE_HOST")
# DATABASE_NAME = os.getenv("DATABASE_NAME")
# DATABASE_PORT = os.getenv("DATABASE_PORT")
# DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
# DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

# DATABASE_URL = f"{DATABASE_CLIENT}://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

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
