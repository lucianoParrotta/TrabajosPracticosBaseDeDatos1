from db_config import conectar

def agregar_producto(nombre, categoria, precio, stock):
        """Agrega un nuevo producto a la base de datos"""
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Productos (nombre, categoria, precio, stock)
                    VALUES (%s, %s, %s, %s)
                """, (nombre, categoria, precio, stock))
                conexion.commit()
                print("Producto agregado exitosamente")
            except Exception as e:
                print(f"Error al agregar producto: {e}")
            finally:
                conexion.close()

def ver_productos():
    """Muestra todos los productos en la base de datos y los devuelve"""
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM Productos")
            productos = cursor.fetchall()  # Recupera los productos
            return productos  # Devuelve la lista de productos
        except Exception as e:
            print(f"Error al mostrar productos: {e}")
            return []  # Retorna una lista vacía en caso de error
        finally:
            conexion.close()

def actualizar_producto(id_producto, nombre=None, categoria=None, precio=None, stock=None):
    """Actualiza los datos de un producto"""
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        try:
            query = 'UPDATE Productos SET nombre=%s, categoria=%s, precio=%s, stock=%s WHERE id=%s'
            params = (nombre, categoria, precio, stock, id_producto) 
            cursor.execute(query, params)
            conexion.commit()
            print("Producto actualizado exitosamente")
        except Exception as e:
            print(f"Error al actualizar producto: {e}")
        finally:
            conexion.close()

def eliminar_producto(id_producto):
        """Eliminar un producto por ID"""
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("DELETE FROM Productos WHERE id = %s", (id_producto,))
                conexion.commit()
                print("Producto eliminado exitosamente")
            except Exception as e:
                print(f"Error al eliminar producto: {e}")
            finally:
                conexion.close()
