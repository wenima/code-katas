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

#helper function
def find_city(city):
    indices = []
    for d in data:
        if d['city'] == city:
            indices.append(data.index(d))
    if indices:
        return indices
    else:
        raise KeyError

def neighbors(n):
        """Return list of neighbors nodes to node n."""
        return [edge for edge in g[n]]

#traversal algorithm
def bfs(start, destination=None):
        """Launch a bfs search, exploring all nodes."""
        q = Queue()
        visited = []
        return explore_bfs(start, q, visited, destination)

def explore_bfs(node, queue, visited, destination=None):
        dist = 0
        has_path = False
        if node not in visited:
            visited.append(node)
            if neighbors(node):
                for neighbor in neighbors(node):
                    if neighbor not in visited:
                        visited.append(neighbor)
                        dist += g[node][neighbor]
                        if neighbor in destination:
                            has_path = True
                            return visited
                        queue.enqueue(neighbor)
                while len(queue):
                    explore_bfs(queue.dequeue(), queue, visited)
        return (visited, dist, has_path)

def flight_path(start, destination):
    start_airports = []
    destination_airports = []
    has_path = False
    for i in find_city(start):
        start_airports.append(data[i]['airport'])
    for i in find_city(destination):
        destination_airports.append(data[i]['airport'])
    try:
        for airport in start_airports:
            returnvalue = bfs(airport, destination_airports )
            if returnvalue[2]:
                path, distance, has_path = returnvalue
                break
    except KeyError:
        return "City has no airport accoring to Wikipedia"
    if has_path:
        print("To get from {0} to {1}, we visited the following airports: {2}. The total distance covered was {3}".format(
    start, destination, path, distance))
    else:
        print("There is no path between {0} and {1}.".format(start, destination))
