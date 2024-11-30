import mysql.connector

def conectar():
    """Establecer la conexión con la base de datos."""
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",          
            user="root",               
            password="43972099",  
            database="sistema_ventas"  
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def obtener_conexion():
    """Retorna la conexión a la base de datos usando la función conectar()"""
    return conectar()  
    