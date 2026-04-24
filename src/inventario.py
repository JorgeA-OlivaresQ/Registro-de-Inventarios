from scr.productos import Producto


class Inventario:
    """
    Gestiona las operaciones del inventario.
    """

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, codigo: str, nombre: str, categoria: str, cantidad: int, stock_minimo: int, precio: float) -> None:
        if codigo in self.productos:
            raise ValueError("Ya existe un producto con ese código.")

        producto = Producto(codigo, nombre, categoria, cantidad, stock_minimo, precio)
        self.productos[codigo] = producto

    def editar_producto(
        self,
        codigo: str,
        nombre: str = None,
        categoria: str = None,
        cantidad: int = None,
        stock_minimo: int = None,
        precio: float = None,
    ) -> None:
        if codigo not in self.productos:
            raise ValueError("Producto no encontrado.")

        producto = self.productos[codigo]

        if nombre is not None and nombre.strip():
            producto.nombre = nombre

        if categoria is not None and categoria.strip():
            producto.categoria = categoria

        if cantidad is not None:
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            producto.cantidad = cantidad

        if stock_minimo is not None:
            if stock_minimo < 0:
                raise ValueError("El stock mínimo no puede ser negativo.")
            producto.stock_minimo = stock_minimo

        if precio is not None:
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            producto.precio = precio

    def eliminar_producto(self, codigo: str) -> None:
        if codigo not in self.productos:
            raise ValueError("Producto no encontrado.")
        del self.productos[codigo]

    def buscar_producto(self, codigo: str) -> dict:
        if codigo not in self.productos:
            raise ValueError("Producto no encontrado.")
        return self.productos[codigo].mostrar_informacion()

    def listar_productos(self) -> list:
        return [producto.mostrar_informacion() for producto in self.productos.values()]

    def registrar_entrada(self, codigo: str, cantidad: int) -> None:
        if codigo not in self.productos:
            raise ValueError("Producto no encontrado.")
        self.productos[codigo].registrar_entrada(cantidad)

    def registrar_salida(self, codigo: str, cantidad: int) -> None:
        if codigo not in self.productos:
            raise ValueError("Producto no encontrado.")
        self.productos[codigo].registrar_salida(cantidad)
