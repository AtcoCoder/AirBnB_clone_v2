#!/usr/bin/python3
"""Starts flask web app that listen on 0.0.0.0:5000"""
from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City

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


@app.route('/cities_by_states', strict_slashes=False)
def get_cities_by_states():
    """Renders webpage to show cities by states"""
    all_states = storage.all(State)
    states = {state.name: state for state_key, state in all_states.items()}
    state_names = list(states.keys())
    state_names.sort()
    sorted_states = [states[name] for name in state_names]
    all_cities = storage.all(City)
    cities = {city.name: city for city_key, city in all_cities.items()}
    city_names = list(cities.keys())
    city_names.sort()
    sorted_cities = [cities[name] for name in city_names]

    states = {}
    for state in sorted_states:
        state_cities = []
        for city in sorted_cities:
            if state.id == city.state_id:
                state_cities.append(city)
        states[state] = state_cities

    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_session(exe):
    """Closes current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
