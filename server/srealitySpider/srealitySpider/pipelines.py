import os
import psycopg2

class PostgresPipeline:

    def __init__(self):
        ## Create/Connect to database
        self.connection = psycopg2.connect(
            dbname=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USERNAME"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_PORT")
        )
        
        self.cur.execute(""" CREATE TABLE IF NOT EXISTS flats(
            id serial PRIMARY KEY, 
            title text,
            image_url text); """)
        
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()

    def process_item(self, item, spider):
        # define insert statement
        self.cur.execute(""" INSERT INTO flats (title, image_url) VALUES (%s, %s) """, (item["title"], item["image_url"]))
        self.connection.commit()
        return item
    
    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

