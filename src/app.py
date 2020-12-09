import os
import caesar_cipher
import vigenere_cipher
from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@app.route("/caesar", methods=["GET", "POST"])
def caesar():
    if request.method == "POST":
        return render_template("caesar.html",
                               encipher=caesar_cipher.caesar_encipher(request.form["shift"], request.form["message"]))
    else:
        return render_template("caesar.html")


@app.route("/vigenere", methods=["GET", "POST"])
def vigenere():
    if request.method == "POST" and request.form["cipher_option"] == "encipher":
        return render_template("vigenere.html",
                               encipher=vigenere_cipher.vigenere_encipher(request.form["key"], request.form["message"]))
    elif request.method == "POST" and request.form["cipher_option"] == "decipher":
        return render_template("vigenere.html",
                               encipher=vigenere_cipher.vigenere_decipher(request.form["key"], request.form["message"]))

    else:
        return render_template("vigenere.html")


if __name__ == "__main__":
    app.run()
