import random
from points import Point


class Observation(object):
    def __init__(self, from_point_name=None, to_point_name=None):
        self.from_point_name = from_point_name
        self.to_point_name = to_point_name

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "(Observation from_point:{0} to_point:{1})".format(self.from_point, self.to_point)

class DistanceObservation(Observation):
    def __init__(self, from_point_name=None, to_point_name=None, meters=None):
        Observation.__init__(self, from_point_name=from_point_name, to_point_name=to_point_name)
        self.meters = float(meters)
    def __str__(self):
        return repr(self)

    def __repr__(self):
        return ("(DistanceObservation from_point_name:{0} to_point_name:{1} meters:{2})"
            .format(self.from_point_name, self.to_point_name, self.meters))

class DirectionObservation(Observation):
    def __init__(self, from_point_name=None, to_point_name=None, radians=None):
        Observation.__init__(self, from_point_name=from_point_name, to_point_name=to_point_name)
        self.radians = float(radians)
    def __str__(self):
        return repr(self)

    def __repr__(self):
        return ("(DirectionObservation from_point_name:{0} to_point_name:{1} radians:{2})"
            .format(self.from_point_name, self.to_point_name, self.radians))

def add_random_error_to_observation(observation):
    if isinstance(observation, DistanceObservation):
        random_error = random.randint(-100, 100) * 0.01
        observation.meters = observation.meters + random_error
    elif isinstance(observation, DirectionObservation):
        random_error = random.randint(-100, 100) * 0.01
        observation.radians = observation.radians + random_error
    else:
        raise Exception('Unknown tpye of observation')
    return observation

def get_list_of_observations_with_random_errors(list_of_observations=None):
    list_of_errored_observations = []
    for observation in list_of_observations:
        list_of_errored_observations.append(add_random_error_to_observation(observation))
    return list_of_errored_observations
