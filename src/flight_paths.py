"""Module to calculate the following:

* given a starting city and an ending city, will return a path between the two cities (including the two cities)
* also returns the total distance traveled between cities
* appropriately handles the situation where no path exists
* Add to your function a parameter that makes it return the shortest path (lowest distance) between the two cities.
* Add to your function a parameter that makes it return the path with the fewest stops between the two cities.
* Have your function take a parameter for a limit to the distance between any two cities. If specified, your function
returns a path where each city-to-city jump is less than or equal to that limit.

To accomplish the above, it reads a json type file taken from wikipedia.org which holds the routes from any
airport as well as the longitude and latitude of the airport. These are then passed into a given function calc_dist to
set up the weights of each route.
"""

import math
import ujson
from stack import Stack


g = {}

JSON_FILE = 'airports_not_clean.json'

def calc_dist(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
    """

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3 # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934 # convert km to miles

#read in all the airport data
with open(JSON_FILE) as airportfile:
    data = ujson.load(airportfile)

#create a small lookup dict of airports + latlong
airports = {value: airport_dict['lat_lon'] for airport_dict in data for key, value in airport_dict.items() if key == 'airport'}
#create a small lookup dict of airports and their possible destinations
routes = {value: airport_dict['destination_airports'] for airport_dict in data for key, value in airport_dict.items() if key == 'airport'}


def add_edges(n1, weight=0):
    """Add edge to graph, if nodes not in graph, add them."""
    #build a dict w distance between n1 and it's destination_cities."""
    edges = {}
    for c in routes[n1]:
        if c in airports:
            edges[c] = calc_dist(airports[n1], airports[c])
        else:
            g[c] = []
    if edges:
        g.update({n1: edges})

def initialize():
    """Set up a weighted graph by filling the dict structure with vertices and edges."""
    for k in airports:
        add_edges(k)
    #some airports strangely have no routes or destinations, we will ad them anyway
    for airport in airports.keys():
        if k not in g.keys():
            g[airport] = []

#helper functions
def find_city(city):
    """Return all indices of occurences of a given City in the list of data."""
    indices = []
    for d in data:
        if d['city'] == city:
            indices.append(data.index(d))
    return indices if indices else raise KeyError

def random_airport_from_city(city):
    """Return a randomly selected airport from a given city."""
    try:
        return data[random.choice(find_city(city))]['airport']
    except KeyError:
        return "City has no airport accoring to Wikipedia"
