


class Point(object):
	def __init__(self, name, z):
		self.name = name
		self.z = z

class HeightObservation(object):
	def __init__(self, from, to, obs_value):
		self.from_ = from_
		self.to = to
		self.obs_value = obs_value

def read_obs(filename='obs.txt'):
	observations = list()
	with open(filename, 'r') as f:
		for line in f:
			parts = line.split(delim)
			from_ = parts[0]
			to = parts[1]
			obs_value = parts[2]
			obs = HeightObservation(from_, to, obs_value)
			observations.append(obs)
	return observations

