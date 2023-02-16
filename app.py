'''
Flask app to host an online instance of the BeeCryptor
@author Cayden Wright
2/16/2023
'''
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def handle():
    if request.method=="GET":
        return render_template("index.html")


if __name__=="__main__":
    app.run()