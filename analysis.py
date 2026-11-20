# implementacion de las siguientes funcionalidades desde el data.json
# total facturado 
# ventas por categoria
# producto mas vendido

def total_facturado(data):
    total = 0
    for venta in data['ventas']:
        total += venta['cantidad'] * venta['precio_unitario']
    return total

def ventas_por_categoria(data):
    ventas = {}
    for venta in data['ventas']:
        categoria = venta['categoria']
        if categoria not in ventas:
            ventas[categoria] = 0
        ventas[categoria] += venta['cantidad'] * venta['precio_unitario']
    return ventas

def producto_mas_vendido(data):
    productos = {}
    for venta in data['ventas']:
        producto = venta['producto']
        if producto not in productos:
            productos[producto] = 0
        productos[producto] += venta['cantidad']
    return max(productos, key=productos.get)

if __name__ == "__main__":
    import json
    from pathlib import Path

    data_path = Path(__file__).with_name("data.json")
    with data_path.open(encoding="utf-8") as f:
        data = json.load(f)

    print("Total facturado:", total_facturado(data))
    print("Ventas por categoria:", ventas_por_categoria(data))
    print("Producto mas vendido:", producto_mas_vendido(data))