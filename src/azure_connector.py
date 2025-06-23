import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

def get_sql_connection():
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('AZURE_SQL_SERVER')};"
        f"DATABASE={os.getenv('AZURE_SQL_DB')};"
        f"UID={os.getenv('AZURE_SQL_USER')};"
        f"PWD={os.getenv('AZURE_SQL_PWD')};"
    )
    print("✅ Connected to Azure SQL")
    return conn
