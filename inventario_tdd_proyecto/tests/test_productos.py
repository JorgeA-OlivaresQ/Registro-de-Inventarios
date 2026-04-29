import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.services import InventarioService


class TestProductos(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine("sqlite:///:memory:")
        TestingSessionLocal = sessionmaker(bind=self.engine)
        Base.metadata.create_all(bind=self.engine)
        self.db = TestingSessionLocal()
        self.service = InventarioService(self.db)

    def tearDown(self):
        self.db.close()

    def test_registrar_producto_correctamente(self):
        producto = self.service.registrar_producto("P001", "Laptop", "Tecnología", 10, 2500.0)
        self.assertEqual(producto.codigo, "P001")
        self.assertEqual(producto.nombre, "Laptop")
        self.assertEqual(producto.cantidad, 10)

    def test_no_permite_codigo_duplicado(self):
        self.service.registrar_producto("P001", "Laptop", "Tecnología", 10, 2500.0)
        with self.assertRaises(ValueError):
            self.service.registrar_producto("P001", "Mouse", "Accesorios", 5, 50.0)

    def test_no_permite_cantidad_negativa(self):
        with self.assertRaises(ValueError):
            self.service.registrar_producto("P002", "Teclado", "Accesorios", -1, 100.0)

    def test_no_permite_precio_negativo(self):
        with self.assertRaises(ValueError):
            self.service.registrar_producto("P003", "Monitor", "Tecnología", 5, -200.0)


if __name__ == "__main__":
    unittest.main()
