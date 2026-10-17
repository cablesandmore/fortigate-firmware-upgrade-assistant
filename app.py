from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open("data/firmware_paths.json") as f:
    firmware_data = json.load(f)

with open("data/known_errors.json") as f:
    error_data = json.load(f)

@app.route("/", methods=["GET", "POST"])
def home():

    resultado = None
    error_info = None

    if request.method == "POST":

        modelo = request.form.get("modelo")
        version = request.form.get("version")
        error_text = request.form.get("error_text")

        if modelo and version:
            try:
                resultado = firmware_data[modelo][version]
            except KeyError:
                resultado = [
                    "No se encontró una ruta definida para esa versión."
                ]

        if error_text:
            error_info = error_data.get(error_text)

    return render_template(
        "index.html",
        resultado=resultado,
        error_info=error_info
    )

if __name__ == "__main__":
    app.run(debug=True)
