# Zoolandia
# To build a zoo, we need to start with the following MVP features.
# A base Animal class.
# A base Species class.
# A class definition for 8 animals that will be the initial exhibits of the zoo. Each one derives from the base Animal class.
# A class definition for the species of our 8 animals, which derive from the base Species class.
# Each animal will be designated as a walking, flying, or swimming animal by inheriting from the appropriate class.
# The species of an animal will be composed into the specific animal instance.
# A base Habitat class.
# A class definition for each habitat we need in our zoo to hold our initial 8 animals.
# Each habitat will hold at least one animal, as an aggregation.
class Animal:

	def __init__(self):
		self.species = None
		self.name = ''

class Species:

	def __init__(self):
		self.common_name = ''
		self.geo_region = ''

class Habitat:

	def __init__(self):
		self.name = ''
		self.members = set()
