#!/usr/bin/python3
"""My web application"""
from flask import Flask, render_template


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


@app.route('/python/', strict_slashes=False)
def python_():
    """python is cool"""
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """displays text along with python"""
    new_text = text.replace('_', ' ')
    return f"Python {new_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Check if is a number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """renders number into template"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Check if number is odd or even and display on browser"""
    state = 'odd'
    if n % 2 == 0:
        state = 'even'
    text = f"Number: {n} is {state}"
    return render_template('6-number_odd_or_even.html', text=text)


if __name__ == "__main__":
    app.run()
