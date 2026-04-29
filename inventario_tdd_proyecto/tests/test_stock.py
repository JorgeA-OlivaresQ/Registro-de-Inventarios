import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.services import InventarioService


class TestStock(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine("sqlite:///:memory:")
        TestingSessionLocal = sessionmaker(bind=self.engine)
        Base.metadata.create_all(bind=self.engine)
        self.db = TestingSessionLocal()
        self.service = InventarioService(self.db)
        self.service.registrar_producto("P001", "Laptop", "Tecnología", 10, 2500.0)

    def tearDown(self):
        self.db.close()

    def test_registrar_entrada_incrementa_stock(self):
        producto = self.service.registrar_entrada("P001", 5)
        self.assertEqual(producto.cantidad, 15)

    def test_registrar_salida_reduce_stock(self):
        producto = self.service.registrar_salida("P001", 4)
        self.assertEqual(producto.cantidad, 6)

    def test_no_permite_salida_con_stock_insuficiente(self):
        with self.assertRaises(ValueError):
            self.service.registrar_salida("P001", 20)

    def test_no_permite_entrada_invalida(self):
        with self.assertRaises(ValueError):
            self.service.registrar_entrada("P001", 0)

    def test_no_permite_salida_invalida(self):
        with self.assertRaises(ValueError):
            self.service.registrar_salida("P001", 0)


if __name__ == "__main__":
    unittest.main()
