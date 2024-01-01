#!/usr/bin/python3
"""Starts flask web app that listen on 0.0.0.0:5000"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def get_states():
    """Renders webpage to show all states"""
    all_states = storage.all(State)
    states = [state for state_key, state in all_states.items()]
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_session(exception):
    """Closes current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
