def transform_data(clientes, productos, ventas):
    clientes.columns = clientes.columns.str.lower()
    productos.columns = productos.columns.str.lower()
    ventas.columns = ventas.columns.str.lower()

    return clientes, productos, ventas