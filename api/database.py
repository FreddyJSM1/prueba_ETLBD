import sys
import os
from sqlalchemy import create_engine

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

ETL_DIR = os.path.join(ROOT_DIR, "etl")

sys.path.append(ETL_DIR)

from config import DB_TARGET

DATABASE_URL = (
    f"mysql+pymysql://{DB_TARGET['user']}:"
    f"{DB_TARGET['password']}@"
    f"{DB_TARGET['host']}/"
    f"{DB_TARGET['database']}"
)

engine = create_engine(DATABASE_URL)