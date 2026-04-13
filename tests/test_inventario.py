from src.productos import Producto
from src.inventario import Inventario
import pytest


# =========================
# TESTS PARA PRODUCTO
# =========================

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


def test_registrar_salida():
    producto = Producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)
    producto.registrar_salida(5)
    assert producto.cantidad == 5


def test_stock_bajo():
    producto = Producto("P001", "Laptop", "Tecnologia", 5, 5, 2500.0)
    assert producto.stock_bajo() is True


# =========================
# TESTS PARA INVENTARIO
# =========================

def test_agregar_producto():
    inv = Inventario()
    inv.agregar_producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)

    assert "P001" in inv.productos


def test_agregar_producto_repetido():
    inv = Inventario()
    inv.agregar_producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)

    with pytest.raises(ValueError):
        inv.agregar_producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)


def test_buscar_producto():
    inv = Inventario()
    inv.agregar_producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)

    producto = inv.buscar_producto("P001")
    assert producto["nombre"] == "Laptop"


def test_eliminar_producto():
    inv = Inventario()
    inv.agregar_producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)

    inv.eliminar_producto("P001")
    assert "P001" not in inv.productos


def test_registrar_entrada_inventario():
    inv = Inventario()
    inv.agregar_producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)

    inv.registrar_entrada("P001", 5)
    assert inv.productos["P001"].cantidad == 15


def test_registrar_salida_inventario():
    inv = Inventario()
    inv.agregar_producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)

    inv.registrar_salida("P001", 5)
    assert inv.productos["P001"].cantidad == 5


def test_listar_productos():
    inv = Inventario()
    inv.agregar_producto("P001", "Laptop", "Tecnologia", 10, 5, 2500.0)

    productos = inv.listar_productos()
    assert len(productos) == 1
