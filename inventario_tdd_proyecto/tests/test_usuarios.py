import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.services import UsuarioService


class TestUsuarios(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine("sqlite:///:memory:")
        TestingSessionLocal = sessionmaker(bind=self.engine)
        Base.metadata.create_all(bind=self.engine)
        self.db = TestingSessionLocal()
        self.service = UsuarioService(self.db)

    def tearDown(self):
        self.db.close()

    def test_registrar_usuario_correctamente(self):
        usuario = self.service.registrar_usuario("admin", "1234", "administrador")
        self.assertEqual(usuario.username, "admin")
        self.assertEqual(usuario.rol, "administrador")

    def test_no_permite_usuario_duplicado(self):
        self.service.registrar_usuario("admin", "1234", "administrador")
        with self.assertRaises(ValueError):
            self.service.registrar_usuario("admin", "5678", "consulta")

    def test_autenticar_usuario_valido(self):
        self.service.registrar_usuario("admin", "1234", "administrador")
        usuario = self.service.autenticar("admin", "1234")
        self.assertEqual(usuario.username, "admin")

    def test_rechaza_credenciales_invalidas(self):
        self.service.registrar_usuario("admin", "1234", "administrador")
        with self.assertRaises(ValueError):
            self.service.autenticar("admin", "0000")


if __name__ == "__main__":
    unittest.main()
