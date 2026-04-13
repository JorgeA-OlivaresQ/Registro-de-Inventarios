from src.inventario import Producto
import pytest

def test_crear_producto_valido():
    producto = Producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)
    assert producto.nombre == "Laptop"
    assert producto.cantidad == 10

def test_codigo_vacio():
    with pytest.raises(ValueError):
        Producto("", "Laptop", "Tecnologia", 10, 5, 2500.0)
      
def test_cantidad_negativa():
    with pytest.raises(ValueError):
        Producto("P001", "Laptop", "Tecnologia", -1, 5, 2500.0)

def test_registrar_entrada():
    producto = Producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)
    producto.registrar_entrada(5)
    assert producto.cantidad == 15

def test_registrar_entrada_invalida():
    producto = Producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)
    with pytest.raises(ValueError):
        producto.registrar_entrada(0)

def test_registrar_salida():
    producto = Producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)
    producto.registrar_salida(5)
    assert producto.cantidad == 5

def test_salida_mayor_stock():
    producto = Producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)
    with pytest.raises(ValueError):
        producto.registrar_salida(20)

def test_stock_bajo():
    producto = Producto("P001", "Laptop", "Tecnologia", 5, 5, 2500.0)
    assert producto.stock_bajo() is True

def test_mostrar_informacion():
    producto = Producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)
    info = producto.mostrar_informacion()
    assert info["nombre"] == "Laptop"
    assert info["stock_bajo"] is False
