from sqlalchemy import create_engine, text
from config import DB_TARGET

def create_database():
    url = f"mysql+pymysql://{DB_TARGET['user']}:{DB_TARGET['password']}@{DB_TARGET['host']}"
    engine = create_engine(url)

    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_TARGET['database']}"))

def load_data (clientes, productos, ventas):
    url = f"mysql+pymysql://{DB_TARGET['user']}:{DB_TARGET['password']}@{DB_TARGET['host']}/{DB_TARGET['database']}"
    engine = create_engine(url)

    clientes.to_sql("clientes", engine, if_exists="replace", index=False)
    productos.to_sql("productos", engine, if_exists="replace", index=False)
    ventas.to_sql("ventas", engine, if_exists="replace", index=False)
    