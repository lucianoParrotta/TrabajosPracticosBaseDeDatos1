from db_config import conectar

from db_config import conectar

def productos_mas_vendidos():
    """Generar un reporte de los productos más vendidos."""
    conexion = conectar()  
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT 
                    p.nombre AS producto,
                    p.categoria,
                    SUM(o.cantidad) AS cantidad_vendida
                FROM Ordenes o
                INNER JOIN Productos p ON o.producto_id = p.id
                GROUP BY o.producto_id
                ORDER BY cantidad_vendida DESC
                LIMIT 10
            """)
            productos = cursor.fetchall()  # Recuperar todos los productos más vendidos
            if not productos:
                return []  # Si no hay productos, devuelve una lista vacía
            return productos 

        except Exception as e:
            print(f"Error al generar el reporte: {e}")
            return []  # En caso de error, retorna una lista vacía

        finally:
            conexion.close() 