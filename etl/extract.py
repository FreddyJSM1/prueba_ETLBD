import pandas as pd
from sqlalchemy import create_engine
from config import DB_SOURCE

def get_connection():
    url = f"mysql+pymysql://{DB_SOURCE['user']}:{DB_SOURCE['password']}@{DB_SOURCE['host']}/{DB_SOURCE['database']}"
    return create_engine(url)

def extract_data():
    engine = get_connection()

    clientes = pd.read_sql("SELECT * FROM clientes", engine)
    productos = pd.read_sql("SELECT * FROM productos", engine)
    ventas = pd.read_sql("SELECT * FROM ventas", engine)

    return clientes, productos, ventas