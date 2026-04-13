from inventario import Inventario


def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("4. Buscar producto")
    print("5. Listar productos")
    print("6. Registrar entrada")
    print("7. Registrar salida")
    print("8. Salir")


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número entero válido.")


def leer_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número decimal válido.")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                codigo = input("Código: ").strip()
                nombre = input("Nombre: ").strip()
                categoria = input("Categoría: ").strip()
                cantidad = leer_entero("Cantidad inicial: ")
                stock_minimo = leer_entero("Stock mínimo: ")
                precio = leer_decimal("Precio: ")

                inventario.agregar_producto(codigo, nombre, categoria, cantidad, stock_minimo, precio)
                print("Producto agregado correctamente.")

            elif opcion == "2":
                codigo = input("Código del producto a editar: ").strip()
                print("Deje en blanco los campos que no desea modificar.")

                nombre = input("Nuevo nombre: ").strip()
                categoria = input("Nueva categoría: ").strip()
                cantidad_txt = input("Nueva cantidad: ").strip()
                stock_minimo_txt = input("Nuevo stock mínimo: ").strip()
                precio_txt = input("Nuevo precio: ").strip()

                cantidad = int(cantidad_txt) if cantidad_txt else None
                stock_minimo = int(stock_minimo_txt) if stock_minimo_txt else None
                precio = float(precio_txt) if precio_txt else None

                inventario.editar_producto(
                    codigo,
                    nombre=nombre if nombre else None,
                    categoria=categoria if categoria else None,
                    cantidad=cantidad,
                    stock_minimo=stock_minimo,
                    precio=precio,
                )
                print("Producto editado correctamente.")

            elif opcion == "3":
                codigo = input("Código del producto a eliminar: ").strip()
                inventario.eliminar_producto(codigo)
                print("Producto eliminado correctamente.")

            elif opcion == "4":
                codigo = input("Código del producto a buscar: ").strip()
                producto = inventario.buscar_producto(codigo)
                print(producto)

            elif opcion == "5":
                productos = inventario.listar_productos()
                if not productos:
                    print("No hay productos registrados.")
                else:
                    for producto in productos:
                        print(producto)

            elif opcion == "6":
                codigo = input("Código del producto: ").strip()
                cantidad = leer_entero("Cantidad de entrada: ")
                inventario.registrar_entrada(codigo, cantidad)
                print("Entrada registrada correctamente.")

            elif opcion == "7":
                codigo = input("Código del producto: ").strip()
                cantidad = leer_entero("Cantidad de salida: ")
                inventario.registrar_salida(codigo, cantidad)
                print("Salida registrada correctamente.")

            elif opcion == "8":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida. Intente nuevamente.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
