from extract import extract_data
from transform import transform_data
from load import create_database, load_data

def run_etl():
    print("Extrayendo datos")
    clientes, productos, ventas = extract_data()

    print("Tranformando datos")
    clientes, productos, ventas = transform_data(clientes, productos, ventas)

    print("Creando base de datos destino")
    create_database()

    print("Cargando datos en la nueva base de datos")
    load_data(clientes, productos, ventas)

    print("Proceso Completado")

if __name__ == "__main__":
    run_etl()
