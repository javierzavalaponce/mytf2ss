from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/herramienta", methods=["GET", "POST"])
def herramienta():
    if request.method == "POST":
        num = request.form["num"]
        den = request.form["den"]

        return f"Numerador recibido: {num}<br>Denominador recibido: {den}"

    return render_template("herramienta.html")


if __name__ == "__main__":
    app.run(debug=True)