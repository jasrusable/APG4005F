


class Point(object):
	def __init__(self, name, type_, x, y, z):
		self.name = name
		self.type_ = type_
		self.x = x
		self.y = y
		self.z = z

class Observation(object):
	def __init__(self, from_, to, type_, value):
		self.from_ = from_
		self.to = to
		self.value = value
		self.type_ = type_

def read_points(filepath='points.txt', delim=','):
	points = list()
	with open (filepath, 'r') as f:
		for line in f:
			if line.startswith('#'):
				continue
			line_parts = line.split(delim)
			name = line_parts[0]
			type_ = line_parts[1]
			x = line_parts[2]
			y = line_parts[3]
			z = line_parts[4]
			points.append(Point(name, type_, x, y, z))
	return points

def read_observations(type_, known_points, filepath='obs.txt', delim=','):
	assert(type_ in ['distance', 'direction'])
	observations = list()
	known_point_names = list()
	for point in known_points:
		known_point_names.append(point.name)
	with open(filepath, 'r') as f:
		for line in f:
			if line.startswith('#'):
				continue
			line_parts = line.split(delim)
			from_ = parts[0]
			if from_ not in known_point_names:
				raise Exception('{0} not defined in known_points.'.format(from_))
			to = parts[1]
			if to not in known_point_names:
				raise Exception('{0} not defined in known_points.'.format(to))
			value = parts[2]
			observations.append(Observation(from_, to, type_, value))
	return observations

points = read_points(filepath='points.txt')
read_observations(type_='distance', known_points=points, filepath='dist_obs.txt')