#!/usr/bin/python3
"""Starts flask web app that listen on 0.0.0.0:5000"""
from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def get_states():
    """Renders webpage to show all states"""
    all_states = storage.all(State)
    states = {state.name: state for state_key, state in all_states.items()}
    state_names = list(states.keys())
    state_names.sort()
    sorted_states = [states[name] for name in state_names]

    return render_template('7-states_list.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def get_state_by_id(id):
    """Renders webpage to show cities by states"""
    key = f"State.{id}"
    all_states = storage.all(State)
    if key in all_states:
        state = all_states[key]
        all_cities = storage.all(City)
        cities = {city.name: city for city_key, city in all_cities.items()}
        state_cities = []
        for city_name, city in cities.items():
            if state.id == city.state_id:
                state_cities.append(city)
        city_names = [city.name for city in state_cities]
        city_names.sort()
        state_sorted_cities = [cities[name] for name in city_names]

        return render_template(
            '9-states.html',
            state=state,
            cities=state_sorted_cities)
    else:
        return render_template('not_found.html')


@app.teardown_appcontext
def teardown_session(exe):
    """Closes current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
