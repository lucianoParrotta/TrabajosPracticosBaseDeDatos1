from db_config import conectar
from CRUD_productos import agregar_producto, ver_productos, actualizar_producto, eliminar_producto

def registrar_cliente(nombre, correo, telefono=None):
        """Registra un nuevo cliente"""
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Clientes (nombre, correo, telefono)
                    VALUES (%s, %s, %s)
                """, (nombre, correo, telefono))
                conexion.commit()
                print("Cliente registrado exitosamente")
            except Exception as e:
                print(f"Error al registrar cliente: {e}")
            finally:
                conexion.close()

def ver_clientes():
    """Devuelve todos los clientes en la base de datos"""
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM Clientes")
            clientes = cursor.fetchall() 
            return clientes
        except Exception as e:
            print(f"Error al mostrar clientes: {e}")
            return []  
        finally:
            conexion.close()

def actualizar_cliente(id_cliente, nombre=None, correo=None, telefono=None):
    """Actualiza los datos de un cliente existente"""
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        try:
            query = "UPDATE Clientes SET nombre=%s, correo=%s, telefono=%s WHERE id=%s"
            params = (nombre, correo, telefono, id_cliente)  
            cursor.execute(query, params)
            conexion.commit()
            print("Cliente actualizado exitosamente")
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
        finally:
            conexion.close()


