from flask import Flask

# Crear la aplicación
app = Flask(__name__)

# Definir una ruta
@app.route("/")
def home():
    return "¡Hola desde Flask!"

# Ejecutar servidor
if __name__ == "__main__":
    app.run(debug=True)
