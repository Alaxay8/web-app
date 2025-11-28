#!/usr/bin/python3

from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, from Python!</h1>. I'm Alex."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
