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
    states = {state.name: state for state_key, state in all_states.items()}
    state_names = list(states.keys())
    state_names.sort()
    sorted_states = [states[name] for name in state_names]

    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_session(exe):
    """Closes current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
