import psycopg2

class PostgresPipeline:

    def __init__(self):
        ## Connection Details
        hostname = 'db'
        username = 'postgres'
        password = 'postgres' 
        database = 'flats'

        ## Create/Connect to database
        self.connection = psycopg2.connect(
            host=hostname, 
            user=username, 
            password=password, 
            dbname=database
        )
        
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS flats(
            id serial PRIMARY KEY, 
            title text,
            image_url text
        )
        """)

    def process_item(self, item, spider):
        # define insert statement
        self.cur.execute(""" INSERT INTO flats (title, image_url) VALUES (%s, %s) """, (item["title"], item["image_url"]))
        self.connection.commit()
        return item
    
    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

