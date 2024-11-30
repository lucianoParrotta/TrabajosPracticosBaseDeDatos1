#  Justificación del Diseño



# 1. Tabla Productos

## Estructura

La tabla Productos almacena información sobre los productos disponibles para la venta, con los siguientes atributos:

   - id (clave primaria): Identifica de manera única cada producto.
   - nombre: Nombre del producto.
   - categoria: Categoría a la que pertenece el producto.
   - precio: Precio del producto.
   - stock: Cantidad disponible en inventario.

## Dependencias Funcionales

   - id -> nombre, categoria, precio, stock: El id identifica de manera única a cada producto y determina los valores de los demás atributos.

## Evaluación de Normalización

1.	Primera Forma Normal (1NF):
   - Todos los atributos son atómicos (no contienen listas ni conjuntos).
   - No hay conjuntos repetitivos en la tabla.
2. Segunda Forma Normal (2NF):
   - La clave primaria es simple (id), por lo que no existen dependencias parciales. Todos los atributos no clave (nombre, categoria, precio, stock) dependen completamente de la clave primaria.
3. Tercera Forma Normal (3NF):
   - No hay dependencias transitivas. Todos los atributos no clave (nombre, categoria, precio, stock) dependen directamente de la clave primaria (id).
  
# 2. Tabla Clientes

## Estructura

La tabla Clientes almacena información sobre los clientes registrados, con los siguientes atributos:
   - id (clave primaria): Identifica de manera única a cada cliente.
   - nombre: Nombre del cliente.
   - correo: Dirección de correo electrónico única del cliente.
   - telefono: Número de teléfono del cliente.

## Dependencias Funcionales

   - id -> nombre, correo, telefono: El id identifica de manera única a cada cliente y determina los valores de los demás atributos.

## Evaluación de Normalización

1.	Primera Forma Normal (1NF):
   - Todos los atributos son atómicos y no hay conjuntos repetitivos.
2.	Segunda Forma Normal (2NF):
   - La clave primaria es simple (id), lo que garantiza que no existan dependencias parciales. Todos los atributos no clave (nombre, correo, telefono) dependen completamente de la clave primaria.
3.	Tercera Forma Normal (3NF):
   - No hay dependencias transitivas. Los atributos nombre, correo y telefono dependen directamente de la clave primaria (id).

# 3. Tabla Órdenes

## Estructura

La tabla Órdenes registra las compras realizadas por los clientes, con los siguientes atributos:
   - id (clave primaria): Identifica de manera única cada orden.
   - producto_id (clave foránea): Referencia a la tabla Productos.
   - cantidad: Cantidad de productos comprados en la orden.
   - fecha: Fecha en que se realizó la orden.

Dependencias Funcionales

1.	id -> cliente_id, producto_id, cantidad, fecha: El id identifica de manera única cada orden y determina los valores de los demás atributos.
2.	cliente_id -> cliente: Garantizado por la relación foránea con la tabla Clientes.
3.	producto_id -> producto: Garantizado por la relación foránea con la tabla Productos.

Evaluación de Normalización

1.	Primera Forma Normal (1NF):
   - Todos los atributos son atómicos, y no hay conjuntos repetitivos.
2.	Segunda Forma Normal (2NF):
   - La clave primaria es simple (id), por lo que no hay dependencias parciales. Todos los atributos no clave (cliente_id, producto_id, cantidad, fecha) dependen completamente de la clave primaria.
3.	Tercera Forma Normal (3NF):
   - No hay dependencias transitivas. Los atributos no clave dependen directamente de la clave primaria (id) o están normalizados a través de claves foráneas.




