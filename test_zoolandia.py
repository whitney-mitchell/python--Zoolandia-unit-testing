import unittest
import zoolandia

class TestAnimal(unittest.TestCase):

	# @classmethod
	# def setUpClass(self):
	# 	pass

	def test_animal_creation(self):
		a_animal = zoolandia.Betta('orange', 'Bob')
		self.assertEquals(a_animal.species.color, 'orange')
		self.assertEquals(a_animal.name, 'Bob')
		self.assertIsInstance(a_animal, zoolandia.Animal)
		self.assertIsInstance(a_animal.species, zoolandia.Species)
		self.assertIsInstance(a_animal.species, zoolandia.BettaTrifasciata)

	def test_locomotion_initialization(self):
		a_animal = zoolandia.Betta('orange', 'Bob')
		self.assertIsInstance(a_animal.locomotion, set)
		self.assertEquals(0, len(a_animal.locomotion))

	def test_add_locomotion(self):
		a_animal = zoolandia.Betta('orange', 'Bob')
		swim = zoolandia.Swimming()
		a_animal.add_locomotion(swim)
		self.assertIn(swim, a_animal.locomotion)

	def test_remove_locomotion(self):
		a_animal = zoolandia.Betta('orange', 'Bob')
		swim = zoolandia.Swimming()
		walk = zoolandia.Walking()
		a_animal.add_locomotion(walk)
		a_animal.remove_locomotion(swim)
		self.assertNotIn(swim, a_animal.locomotion)
		self.assertIn(walk, a_animal.locomotion)

class TestSpecies(unittest.TestCase):

	def test_commonname_empty_string_default(self):
		species = zoolandia.Species()
		self.assertEquals(species.common_name, '')

	def test_georegion_empty_string_default(self):
		species = zoolandia.Species()
		self.assertEquals(species.geo_region, '')


class TestHabitat(unittest.TestCase):

	def test_name_empty_string_default(self):
		habitat = zoolandia.Habitat()
		self.assertEquals(habitat.name, '')

	def test_members_set_default(self):
		habitat = zoolandia.Habitat()
		self.assertIsInstance(habitat.members, set)

	def test_add_member(self):
		aquarium = zoolandia.Aquarium("freshwater")
		a_animal = zoolandia.Betta('orange', 'Bob')
		aquarium.add_member(a_animal)
		self.assertIn(a_animal, aquarium.members)

	def test_remove_member(self):
		aquarium = zoolandia.Aquarium("freshwater")
		jj = zoolandia.Betta('blue', "JJ")
		aquarium.add_member(jj)
		aquarium.remove_member(jj)
		self.assertNotIn(jj, aquarium.members)

class TestWalking(unittest.TestCase):

	def test_legs_zero_default(self):
		walking = zoolandia.Walking()
		self.assertEquals(walking.legs, 0)

	def test_walk_speed_zero_default(self):
		walking = zoolandia.Walking()
		self.assertEquals(walking.walk_speed, 0)


class TestSwimming(unittest.TestCase):

	def test_appendages(self):
		swimming = zoolandia.Swimming()
		self.assertEquals(swimming.fins, False)
		self.assertEquals(swimming.flippers, False)
		self.assertEquals(swimming.web_feet, False)

	def test_swim_speed_zero_default(self):
		swimming = zoolandia.Swimming()
		self.assertEquals(swimming.swim_speed, 0)


class TestFlying(unittest.TestCase):

	def test_wings_zero_default(self):
		flying = zoolandia.Flying()
		self.assertEquals(flying.wings, 0)

	def test_wing_span_zero_default(self):
		flying = zoolandia.Flying()
		self.assertEquals(flying.wing_span, 0)

	def test_air_speed_zero_default(self):
		flying = zoolandia.Flying()
		self.assertEquals(flying.air_speed, 0)
if __name__ =='__main__':
		unittest.main()
