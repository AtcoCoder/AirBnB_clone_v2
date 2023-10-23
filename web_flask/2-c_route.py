#!/usr/bin/python3
"""My web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """home route function"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb route function"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """Displays our text"""
    new_text = text.replace('_', ' ')
    return f"C {new_text}"


if __name__ == "__main__":
    app.run()
