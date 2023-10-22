from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
