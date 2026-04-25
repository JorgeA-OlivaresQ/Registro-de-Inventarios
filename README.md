# Desarrollo de una plataforma web para un registro de inventarios
## Problema a resolver
El problema identificado consiste en la falta de un sistema organizado para gestionar el inventario de productos. Cuando esta tarea se realiza manualmente, 
suelen presentarse inconsistencias entre el stock real y el registrado, además de retrasos en la actualización de la información. Esto afecta el funcionamiento 
de la organización y dificulta la planificación de reposiciones. 

Como solución, se plantea desarrollar una aplicación web de registro de inventarios. El sistema permitirá ingresar productos con datos básicos, visualizar el 
stock disponible, registrar movimientos de entrada y salida, y generar alertas de stock mínimo. De esta manera, se busca mejorar el control de los recursos y 
facilitar una gestión más ordenada y confiable. 

## Propuesta de solución del módulo de gestión de productos
Se ha creado un notebook para empezar a probar la mejor implementación.

La plataforma web del registro de inventarios que se pretende desarrollar tiene los siguientes módulos:
Módulos del sistema
1. Módulo de autenticación de usuarios: Permite el inicio de sesión y el control de acceso al sistema según el tipo de usuario.
2. Módulo de gestión de productos: Sirve para registrar, editar, eliminar y consultar los productos del inventario.
3. Módulo de control de stock: Permite visualizar la cantidad disponible de cada producto y actualizar existencias.
4. Módulo de entradas de inventario: Registra el ingreso de nuevos productos o la reposición de stock.
5. Módulo de salidas de inventario: Controla la salida de productos por venta, consumo interno o traslado.
6. Módulo de alertas de stock mínimo: Genera avisos cuando un producto alcanza niveles bajos de existencia.
7. Módulo de historial o movimientos: Guarda el registro de todas las entradas y salidas realizadas en el sistema.
8. Módulo de reportes: Permite generar reportes básicos del inventario, productos con bajo stock y movimientos realizados.
9. Módulo de manejo de excepciones y validaciones: Controla errores del sistema y valida que los datos ingresados sean correctos.
10. Módulo de administración: Permite gestionar usuarios, parámetros del sistema y configuraciones generales.
## Actualización
Se realizaron mejoras en la configuración de pruebas automatizadas (CI).
