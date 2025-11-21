from productos.models import Producto
from django.db import connection

def consulta_sql():
    sql = """
        SELECT p.id, p.nombre, p.precio, c.nombre AS categoria
        FROM productos_producto p
        JOIN productos_categoria c ON p.categoria_id = c.id
        WHERE p.precio > %s
        ORDER BY p.precio DESC
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, [1.6])
        rows = cursor.fetchall()
    for row in rows:
        print(f"{row[1]} | ${row[2]} | {row[3]}")

if __name__ == '__main__':
    consulta_sql()