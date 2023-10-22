#!/usr/bin/python3
"""My web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """home route function"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
