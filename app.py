from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("inventario.db")

#  LISTAR PRODUCTOS
@app.route("/")
def index():
    db = get_db()
    productos = db.execute("SELECT * FROM productos").fetchall()
    db.close()
    return render_template("index.html", productos=productos)

#  CREAR PRODUCTO
@app.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nombre = request.form["nombre"]
        categoria = request.form["categoria"]
        precio = request.form["precio"]
        stock = request.form["stock"]

        db = get_db()
        db.execute("INSERT INTO productos (nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)",
                   (nombre, categoria, precio, stock))
        db.commit()
        db.close()
        return redirect("/")

    return render_template("crear.html")

#  EDITAR PRODUCTO
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    db = get_db()

    if request.method == "POST":
        nombre = request.form["nombre"]
        categoria = request.form["categoria"]
        precio = request.form["precio"]
        stock = request.form["stock"]

        db.execute("UPDATE productos SET nombre=?, categoria=?, precio=?, stock=? WHERE id=?",
                   (nombre, categoria, precio, stock, id))
        db.commit()
        db.close()
        return redirect("/")

    producto = db.execute("SELECT * FROM productos WHERE id=?", (id,)).fetchone()
    db.close()
    return render_template("editar.html", producto=producto)

#  ELIMINAR PRODUCTO
@app.route("/eliminar/<int:id>")
def eliminar(id):
    db = get_db()
    db.execute("DELETE FROM productos WHERE id=?", (id,))
    db.commit()
    db.close()
    return redirect("/")

# 🔹 EJECUTAR SERVIDOR
if __name__ == "__main__":
    app.run(debug=True)