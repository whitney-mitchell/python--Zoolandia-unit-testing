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

# For animals.py: just import from species, class Animal:..., class Betta(Animal):...

class Animal:
	def __init__(self, name, species):
		self.species = species
		self.name = name
		self.locomotion = set()

	def add_locomotion(self, loco):
		self.locomotion.add(loco)

	def remove_locomotion(self, loco):
		self.locomotion.discard(loco)

class Species:
	def __init__(self):
		self.common_name = ''
		self.geo_region = ''

class BettaTrifasciata(Species):
	def __init__(self, color):
		self.color = color
		self.common_name = 'Betta'

class Betta(Animal):
	def __init__(self, color, name):
		Animal.__init__(self, name, BettaTrifasciata(color))
# inits a betta that is an animal that inits a BettaTri... that inits a species
# Animal. could instead be super(). (in Python 3), referencing the parent object, here Animal.

class Habitat:
	def __init__(self):
		self.name = ''
		self.members = set()

	def add_member(self, member):
		self.members.add(member)

	def remove_member(self, member):
		self.members.remove(member)

class Aquarium(Habitat):
	def __init__(self, water_type):
		Habitat.__init__(self)
		self.water_type = water_type

class Walking:
	def __init__(self):
		self.walk_speed = 0
		self.legs = 0

class Flying:
	def __init__(self):
		self.air_speed = 0
		self.wings = 0
		self.wing_span = 0

class Swimming:
	def __init__(self):
		self.swim_speed = 0
		self.fins = False
		self.flippers = False
		self.web_feet = False
