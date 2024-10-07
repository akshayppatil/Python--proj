import os
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Get PostgreSQL connection details from environment variables
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')  # Default to 5432 if not set

# Function to create the database if it doesn't exist
def create_database():
    try:
        # Connect to PostgreSQL server (not to a specific database)
        conn = psycopg2.connect(
            dbname="postgres",  # Connect to the default 'postgres' database
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        # Check if the database exists
        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{POSTGRES_DB}';")
        exists = cursor.fetchone()

        if not exists:
            # If the database doesn't exist, create it
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(POSTGRES_DB)))
            print(f"Database '{POSTGRES_DB}' created successfully.")
        else:
            print(f"Database '{POSTGRES_DB}' already exists.")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error creating database: {e}")

# Function to connect to the created database
def get_db_connection():
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=POSTGRES_PORT
    )
    return conn

# Function to create the 'users' table
def create_users_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    '''
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()
