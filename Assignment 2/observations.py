

class Observation(object):
    def __init__(self, from_point=None, to_point=None):
        self.from_point = from_point
        self.to_point = to_point
                 
class DistanceObservation(Observation):
    def __init__(self, from_point=None, to_point=None, value=None):
        Observation.__init__(self, to_point=to_point, from_point=from_point)
        self.value = value

class DirectionObservation(Observation):
    def __init__(self, from_point=None, to_point=None, value=None):
        Observation.__init__(self, to_point=to_point, from_point=from_point)
        self.value = value

