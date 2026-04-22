import sqlite3

conexion = sqlite3.connect("inventario.db")

conexion.execute("""
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL
)
""")

conexion.close()
print("Base de datos creada")