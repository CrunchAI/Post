import psycopg2
from psycopg2 import sql
import io
from PIL import Image

class database:

    def create_database(self, PA_DB: str, DB_NAME: str, DB_USER: str, 
                        DB_PASSWORD: str, DB_HOST: str, DB_PORT: str):
        # Connect to the default 'postgres' database to create our new database
        conn = psycopg2.connect(
            dbname=PA_DB,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cur = conn.cursor()
        
        # Check if the database already exists
        cur.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [DB_NAME])
        exists = cur.fetchone()

        # Create the new database
        if not exists:
            cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
        else:
                print("Database exists")
        
        cur.close()
        conn.close()

    def create_table(self, PA_DB: str, DB_NAME: str, DB_USER: str, 
                        DB_PASSWORD: str, DB_HOST: str, DB_PORT: str):
        # Connect to our new database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        
        # Create the images table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS images (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                data BYTEA NOT NULL,
                upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        cur.close()
        conn.close()

    # def insert_image(image_path, image_name):
    #     conn = psycopg2.connect(
    #         dbname=DB_NAME,
    #         user=DB_USER,
    #         password=DB_PASSWORD,
    #         host=DB_HOST,
    #         port=DB_PORT
    #     )
    #     cur = conn.cursor()
        
    #     # Read the image file
    #     with open(image_path, 'rb') as f:
    #         image_data = f.read()
        
    #     # Insert the image into the database
    #     cur.execute(
    #         "INSERT INTO images (name, data) VALUES (%s, %s)",
    #         (image_name, psycopg2.Binary(image_data))
    #     )
        
    #     conn.commit()
    #     cur.close()
    #     conn.close()

    # def retrieve_image(image_name):
    #     conn = psycopg2.connect(
    #         dbname=DB_NAME,
    #         user=DB_USER,
    #         password=DB_PASSWORD,
    #         host=DB_HOST,
    #         port=DB_PORT
    #     )
    #     cur = conn.cursor()
        
    #     # Retrieve the image from the database
    #     cur.execute("SELECT data FROM images WHERE name = %s", (image_name,))
    #     image_data = cur.fetchone()[0]
        
    #     cur.close()
    #     conn.close()
        
    #     # Convert the binary data back to an image
    #     image = Image.open(io.BytesIO(image_data))
    #     return image

if __name__ == "__main__":
    # Database connection parameters
    PA_DB = "postgres"
    DB_NAME = "bbox_data"
    DB_USER = "admin"
    DB_PASSWORD = "pass"
    DB_HOST = "localhost"
    DB_PORT = "5432"

    db = database()

    db.create_database(PA_DB, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    db.create_table(PA_DB, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    
    # # Example usage
    # insert_image("path/to/your/image.jpg", "example_image")
    # retrieved_image = retrieve_image("example_image")
    # retrieved_image.show()