from .models import Producto, Usuario


class InventarioService:
    def __init__(self, db):
        self.db = db

    def registrar_producto(self, codigo, nombre, categoria, cantidad, precio):
        existente = self.db.query(Producto).filter_by(codigo=codigo).first()
        if existente:
            raise ValueError("Ya existe un producto con ese código.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        producto = Producto(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            cantidad=cantidad,
            precio=precio
        )
        self.db.add(producto)
        self.db.commit()
        self.db.refresh(producto)
        return producto

    def consultar_producto(self, codigo):
        producto = self.db.query(Producto).filter_by(codigo=codigo).first()
        if not producto:
            raise ValueError("Producto no encontrado.")
        return producto

    def registrar_entrada(self, codigo, cantidad):
        producto = self.consultar_producto(codigo)
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        producto.cantidad += cantidad
        self.db.commit()
        self.db.refresh(producto)
        return producto

    def registrar_salida(self, codigo, cantidad):
        producto = self.consultar_producto(codigo)
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        if producto.cantidad < cantidad:
            raise ValueError("Stock insuficiente.")
        producto.cantidad -= cantidad
        self.db.commit()
        self.db.refresh(producto)
        return producto


class UsuarioService:
    def __init__(self, db):
        self.db = db

    def registrar_usuario(self, username, password, rol):
        existente = self.db.query(Usuario).filter_by(username=username).first()
        if existente:
            raise ValueError("El usuario ya existe.")

        usuario = Usuario(
            username=username,
            password=password,
            rol=rol
        )
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def autenticar(self, username, password):
        usuario = self.db.query(Usuario).filter_by(username=username).first()
        if not usuario or usuario.password != password:
            raise ValueError("Credenciales inválidas.")
        return usuario
