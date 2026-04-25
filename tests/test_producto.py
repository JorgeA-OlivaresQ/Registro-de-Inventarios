import unittest
from src.productos import Producto


class TestProducto(unittest.TestCase):

    def test_crear_producto(self):
        producto = Producto("P001", "Laptop", "Tecnología", 10, 5, 2500)

        self.assertEqual(producto.codigo, "P001")
        self.assertEqual(producto.cantidad, 10)


if __name__ == "__main__":
    unittest.main()
