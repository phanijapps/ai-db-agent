import psycopg2
from psycopg2 import pool
import json
from smolagents import tool
import os
from dotenv import load_dotenv

class PostgresUtil:
    _instance = None

    def __new__(cls, minconn=None, maxconn=None, connection_params=None):
        if cls._instance is None:
            cls._instance = super(PostgresUtil, cls).__new__(cls)
            cls._instance.pool = psycopg2.pool.SimpleConnectionPool(
                minconn,
                maxconn,
                host=connection_params['host'],
                database=connection_params['database'],
                user=connection_params['user'],
                password=connection_params['password'],
                port=connection_params.get('port', 5432)  # Default port is 5432
            )
        return cls._instance

    def get_connection(self):
        """Get a connection from the pool."""
        return self.pool.getconn()

    def release_connection(self, connection):
        """Release a connection back to the pool."""
        self.pool.putconn(connection)

    def close_all_connections(self):
        """Close all connections in the pool."""
        self.pool.closeall()

    def execute_query(self, query):
        """Execute a SQL query and return the results."""
        connection = self.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                        # Get column names from the cursor
                colnames = [desc[0] for desc in cursor.description]
    
                # Convert the result to a list of dictionaries
                result = [dict(zip(colnames, row)) for row in rows]
            
            return result
        except psycopg2.Error as e:
            return {"error": str(e)}
        finally:
            self.release_connection(connection)


@tool
def execute_query(sql_query: str) -> str:
    """
    Executes Postgres SQL queries passed as parameter. Returns a json representation of the result. The query can be executed on
    Album table
   
    Args:
        sql_query: The postgres sql query to perform.
    """
    connection = None
    cursor = None
    load_dotenv()
    try:
        # Connection parameters
        connection_params = {
            "host": os.getenv("DB_HOST"),
            "database": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USERNAME"),
            "password": os.getenv("DB_PASSWORD"),
            "port": os.getenv("DB_PORT")
        }

        # Initialize connection pool singleton if not already initialized
        connection_pool = PostgresUtil(minconn=1, maxconn=10, connection_params=connection_params)

        # Return the result 
        return connection_pool.execute_query(sql_query)

    except Exception as e:
        return json.dumps({"error": str(e)})

    finally:
        # Release the connection back to the pool
        if cursor:
            cursor.close()
        if connection:
            connection_pool.release_connection(connection)