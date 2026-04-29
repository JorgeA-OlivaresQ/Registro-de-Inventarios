from app.database import engine, Base, SessionLocal
from app.services import InventarioService, UsuarioService

Base.metadata.create_all(bind=engine)


def main():
    db = SessionLocal()

    inventario_service = InventarioService(db)
    usuario_service = UsuarioService(db)

    try:
        usuario = usuario_service.registrar_usuario("admin", "1234", "administrador")
        print(f"Usuario registrado: {usuario.username}")
    except ValueError as e:
        print(e)

    try:
        producto = inventario_service.registrar_producto("P001", "Laptop", "Tecnología", 10, 2500.0)
        print(f"Producto registrado: {producto.nombre}")
    except ValueError as e:
        print(e)

    db.close()


if __name__ == "__main__":
    main()
