import numpy
import sympy

from points import Point
from observations import Observation
from utils import to_radians
from file_io import read_points, read_observations


points = read_points(filepath='data/points.txt')
#observations = read_observations(type_='distance', known_points=points, filepath='data/dist_obs.txt')
observations = read_observations(type_='direction', known_points=points, filepath='data/dir_obs.txt')

def get_model():
    from_x = sympy.Symbol('from_x')
    from_y = sympy.Symbol('from_y')
    from_z = sympy.Symbol('from_z')
    to_x = sympy.Symbol('to_x')
    to_y = sympy.Symbol('to_y')
    to_z = sympy.Symbol('to_z')
    orientation_correction = sympy.Symbol('orientation_correction')
    true = sympy.Symbol('true')
    sin = sympy.sin
    cos = sympy.cos
    tan = sympy.tan
    atan = sympy.atan
    hz_direction = atan((to_y - from_y)/(to_x - from_x)) - orientation_correction - true
    return hz_direction

def get_A_row(model, observation, points):
    a_row = list()
    print(observation)
    for point in points:
        if point.type_ == 'free':
            x_diff = sympy.diff(model, 'to_x')
            y_diff = sympy.diff(model, 'to_y')
            if point == observation.to:
                print('is to point')
            if point == observation.from_:
                print('is from point')

get_A_row(get_model(), observations[0], points)
get_A_row(get_model(), observations[4], points)
