#!/usr/bin/python3
"""Starts flask web app that listen on 0.0.0.0:5000"""
from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def get_hbnb_filters():
    """Renders webpage to show cities by states"""
    all_states = storage.all(State)
    states = {state.name: state for state_key, state in all_states.items()}
    state_names = list(states.keys())
    state_names.sort()
    sorted_states = [states[name] for name in state_names]
    all_cities = storage.all(City)
    all_amenities = storage.all(Amenity)
    amenities = [amenity for amenity_key, amenity in all_amenities.items()]
    cities = {city.name: city for city_key, city in all_cities.items()}

    states = {}
    for state in sorted_states:
        state_cities = []
        for city_name, city in cities.items():
            if state.id == city.state_id:
                state_cities.append(city)
        city_names = [city.name for city in state_cities]
        city_names.sort()
        state_sorted_cities = [cities[name] for name in city_names]
        states[state] = state_sorted_cities

    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenities)


@app.teardown_appcontext
def teardown_session(exe):
    """Closes current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
