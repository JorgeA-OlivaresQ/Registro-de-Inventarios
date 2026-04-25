from src.productos import Producto


def test_crear_producto():
    producto = Producto("P001", "Laptop", "Tecnología", 10, 5, 2500)

    assert producto.codigo == "P001"
    assert producto.cantidad == 10
