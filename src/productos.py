class Producto:
    """
    Representa un producto dentro del sistema de inventario.
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, cantidad: int, stock_minimo: int, precio: float):
        if not codigo.strip():
            raise ValueError("El código no puede estar vacío.")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        if stock_minimo < 0:
            raise ValueError("El stock mínimo no puede ser negativo.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.cantidad = cantidad
        self.stock_minimo = stock_minimo
        self.precio = precio

    def registrar_entrada(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad de entrada debe ser mayor que cero.")
        self.cantidad += cantidad
        return self.cantidad  # 🔥 útil para tests

    def registrar_salida(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad de salida debe ser mayor que cero.")
        if cantidad > self.cantidad:
            raise ValueError("No hay suficiente stock para realizar la salida.")
        self.cantidad -= cantidad
        return self.cantidad  # 🔥 útil para tests

    def stock_bajo(self) -> bool:
        return self.cantidad <= self.stock_minimo

    def mostrar_informacion(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "cantidad": self.cantidad,
            "stock_minimo": self.stock_minimo,
            "precio": self.precio,
            "stock_bajo": self.stock_bajo(),
        }
