from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open("data/firmware_paths.json") as f:
    firmware_data = json.load(f)


@app.route("/", methods=["GET", "POST"])
def home():

    resultado = None

    if request.method == "POST":

        modelo = request.form["modelo"]
        version = request.form["version"]

        try:
            resultado = firmware_data[modelo][version]
        except KeyError:
            resultado = [
                "No se encontró una ruta definida para esa versión."
            ]

    return render_template(
        "index.html",
        resultado=resultado
    )


if __name__ == "__main__":
    app.run(debug=True)
