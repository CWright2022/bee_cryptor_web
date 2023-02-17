'''
Flask app to host an online instance of the BeeCryptor
@author Cayden Wright
2/16/2023
'''
from flask import Flask, request, render_template, redirect, url_for

from bee_cryptor import encrypt, decrypt

app = Flask(__name__)

OUTPUT_TEXT = ""


@app.route('/', methods=["GET", "POST"])
def handle():
    global OUTPUT_TEXT
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        text = request.form.get("text")
        operation = request.form.get("chooser")
        if operation == "decrypt":
            OUTPUT_TEXT = decrypt(text, "./script.txt")
        else:
            OUTPUT_TEXT = encrypt(text, "./script.txt")
        return redirect(
            url_for('success'))


@app.route("/success")
def success():
    return render_template('success.html', output_text=OUTPUT_TEXT)


if __name__ == "__main__":
    app.run()
