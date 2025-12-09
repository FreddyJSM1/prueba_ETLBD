from fastapi import APIRouter
from sqlalchemy import text
from .database import engine

router = APIRouter()

@router.get("/ventas-por-categoria")
def ventas_por_categoria():
    query = """
        SELECT 
            p.categoria,
            SUM(v.cantidad * p.precio) AS total_ventas
        FROM ventas v
        JOIN productos p ON v.id_producto = p.id_producto
        GROUP BY p.categoria
    """

    with engine.connect() as conn:
        result = conn.execute(text(query))
        data = [dict(row._mapping) for row in result]

    return {
        "status": "ok",
        "total_por_categoria": data
    }