import pytest
from src.productos import Producto


# =========================
# TESTS DE CREACIÓN
# =========================

def test_crear_producto():
    producto = Producto("P001", "Laptop", "Tecnología", 10, 5, 2500)

    assert producto.codigo == "P001"
    assert producto.cantidad == 10


# =========================
# TESTS DE VALIDACIONES
# =========================

def test_codigo_vacio():
    with pytest.raises(ValueError):
        Producto("", "Laptop", "Tecnología", 10, 5, 2500)


def test_cantidad_negativa():
    with pytest.raises(ValueError):
        Producto("P001", "Laptop", "Tecnología", -1, 5, 2500)


def test_precio_negativo():
    with pytest.raises(ValueError):
        Producto("P001", "Laptop", "Tecnología", 10, 5, -100)


# =========================
# TESTS DE OPERACIONES
# =========================

def test_registrar_entrada():
    producto = Producto("P001", "Laptop", "Tecnología", 10, 5, 2500)

    nueva_cantidad = producto.registrar_entrada(5)

    assert nueva_cantidad == 15


def test_registrar_entrada_invalida():
    producto = Producto("P001", "Laptop", "Tecnología", 10, 5, 2500)

    with pytest.raises(ValueError):
        producto.registrar_entrada(0)


def test_registrar_salida():
    producto = Producto("P001", "Laptop", "Tecnología", 10, 5, 2500)

    nueva_cantidad = producto.registrar_salida(5)

    assert nueva_cantidad == 5


def test_salida_excesiva():
    producto = Producto("P001", "Laptop", "Tecnología", 5, 2, 2500)

    with pytest.raises(ValueError):
        producto.registrar_salida(10)


# =========================
# TESTS DE LÓGICA
# =========================

def test_stock_bajo():
    producto = Producto("P001", "Laptop", "Tecnología", 3, 5, 2500)

    assert producto.stock_bajo() is True


def test_mostrar_informacion():
    producto = Producto("P001", "Laptop", "Tecnología", 10, 5, 2500)

    info = producto.mostrar_informacion()

    assert info["codigo"] == "P001"
    assert info["stock_bajo"] is False
