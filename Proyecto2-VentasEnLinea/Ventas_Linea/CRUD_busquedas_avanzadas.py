from db_config import conectar

def buscar_producto(filtro):
    """Busqueda de productos según un filtro por nombre"""
    conexion = conectar()  
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        try:
            query = """
                SELECT id, nombre, categoria, precio, stock 
                FROM Productos
                WHERE nombre LIKE %s
            """
            filtro_like = f"%{filtro}%" 
            cursor.execute(query, (filtro_like,))
            productos = cursor.fetchall()  # Recuperar todos los productos que coinciden con el filtro
            
            if not productos:
                return []  # Retorna una lista vacía si no hay productos
            return productos  

        except Exception as e:
            print(f"Error al realizar la búsqueda: {e}")
            return []  # En caso de error, devuelve una lista vacía

        finally:
            conexion.close() 
            
def buscar_cliente(filtro):
    """Búsqueda de clientes según un filtro por nombre o correo, y los devuelve."""
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT 
                    id,
                    nombre,
                    correo,
                    telefono
                FROM Clientes
                WHERE nombre LIKE %s OR correo LIKE %s
            """, (f"%{filtro}%", f"%{filtro}%"))
            clientes = cursor.fetchall()  
            return clientes  
        except Exception as e:
            print(f"Error al realizar la búsqueda: {e}")
            return []  # Retorna una lista vacía en caso de error
        finally:
            conexion.close()
    return []  # Retorna una lista vacía si no hay conexión