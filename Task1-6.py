"""
 The Resistance maintains hidden bases across the city. Each base is marked on a map by its (x, y) coordinates. Headquarters is located at (0, 0). In case of emergencies, bases closest to HQ will receive evacuation priority.

Write a function calculate_distances(coords) that:

Calculates the Euclidean distance of each base from HQ.

Returns a dictionary mapping each coordinate to its distance, rounded to 2 decimals.
"""


def calculate_distances(coords):
    dist = {}
    for i in coords:
        d = (i[0]**2+i[1]**2)**0.5
        dist[i] = round(d,2)
    return dist

