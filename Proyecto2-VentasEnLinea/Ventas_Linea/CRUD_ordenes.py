from db_config import conectar


def mostrar_ordenes_por_cliente(cliente_id):
     """Muestra todas las órdenes realizadas por un cliente dado y las devuelve."""
     conexion = conectar()
     if conexion:
         cursor = conexion.cursor(dictionary=True)
         try:
             cursor.execute("""
                 SELECT 
                     o.id AS orden_id,
                     p.nombre AS producto,
                     p.categoria,
                     o.cantidad,
                     o.fecha
                 FROM Ordenes o
                 INNER JOIN Productos p ON o.producto_id = p.id
                 WHERE o.cliente_id = %s
                 ORDER BY o.fecha DESC
             """, (cliente_id,))
             ordenes = cursor.fetchall()  
             return ordenes  
         except Exception as e:
             print(f"Error al mostrar órdenes: {e}")
             return []  # Retorna una lista vacía en caso de error
         finally:
             conexion.close()

def modificar_ordenes_para_cantidad_maxima(producto_id, cantidad_maxima):
    """Ajusta las órdenes de un producto para que la cantidad no supere el valor máximo dado."""
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()

            # Iniciar una transacción
            conexion.start_transaction()

            # Ajustar las órdenes con cantidad mayor al máximo
            cursor.execute("""
                UPDATE Ordenes
                SET cantidad = %s
                WHERE producto_id = %s AND cantidad > %s
            """, (cantidad_maxima, producto_id, cantidad_maxima))
            print(f"Órdenes del producto ID {producto_id} ajustadas a un máximo de {cantidad_maxima} unidades.")

            # Confirmar la transacción
            conexion.commit()

            return f"Órdenes del producto con ID {producto_id} ajustadas a un máximo de {cantidad_maxima} unidades."

        except Exception as e:
            conexion.rollback()  # Deshace cambios en caso de error
            print(f"Error al ajustar las órdenes: {e}")
            return f"Error al ajustar las órdenes: {e}"

        finally:
            conexion.close()

def crear_orden(cliente_id, producto_id, cantidad, fecha):
    """Crea una orden en la base de datos."""
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                INSERT INTO Ordenes (cliente_id, producto_id, cantidad, fecha)
                VALUES (%s, %s, %s, %s)
            """, (cliente_id, producto_id, cantidad, fecha))
            conexion.commit()

            return f"Orden para el cliente con ID {cliente_id} y producto con ID {producto_id} creada exitosamente."
        except Exception as e:
            conexion.rollback()
            return f"Error al crear la orden: {e}"
        finally:
            conexion.close()