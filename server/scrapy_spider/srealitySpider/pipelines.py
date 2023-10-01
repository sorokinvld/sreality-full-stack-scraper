import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine.url import URL

Base = declarative_base()

class Flat(Base):
            __tablename__ = 'flats'
            id = Column(Integer, primary_key=True)
            title = Column(String)
            image_url = Column(String)

class PostgresPipeline(object):

    def __init__(self):
        # Create/Connect to database
        url_object = URL.create(
            "postgresql+psycopg2",
            username=os.getenv("DATABASE_USERNAME"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            database=os.getenv("DATABASE_NAME"),
        )
        
        self.flats = Flat
        self.engine = create_engine(url_object)
        Base.metadata.create_all(self.engine)
        self.session = scoped_session(sessionmaker(bind=self.engine))     

    def process_item(self, item, spider):            
        session = self.session()
        instanse = session.query(self.flats).filter_by(**item).one_or_none()
        
        if instanse:
            return instanse
        zelda_item = self.flats(**item)
        
        try:
            self.session.add(zelda_item)
            self.session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        
        return item
