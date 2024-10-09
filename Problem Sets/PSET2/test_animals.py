import unittest
from animals import Mammals, Birds, Reptiles

class TestMammals(unittest.TestCase):
    def setUp(self):
        self.mammals = Mammals()

    def test_outSpecies(self):
        result = self.mammals.outSpecies()
        expected = ['Lion', 'Elephant', 'Tiger', 'Bear']
        self.assertEqual(result, expected)

    def test_addSpecies(self):
        self.mammals.addSpecies('Panda')
        result = self.mammals.outSpecies()
        expected = ['Lion', 'Elephant', 'Tiger', 'Bear', 'Panda']
        self.assertEqual(result, expected)

class TestBirds(unittest.TestCase):
    def setUp(self):
        self.birds = Birds()

    def test_outSpecies(self):
        result = self.birds.outSpecies()
        expected = ['Eagle', 'Parrot', 'Penguin', 'Owl']
        self.assertEqual(result, expected)

    def test_addSpecies(self):
        self.birds.addSpecies('Flamingo')
        result = self.birds.outSpecies()
        expected = ['Eagle', 'Parrot', 'Penguin', 'Owl', 'Flamingo']
        self.assertEqual(result, expected)

class TestReptiles(unittest.TestCase):
    def setUp(self):
        self.reptiles = Reptiles()

    def test_outSpecies(self):
        result = self.reptiles.outSpecies()
        expected = ['Crocodile', 'Lizard', 'Snake', 'Turtle']
        self.assertEqual(result, expected)

    def test_addSpecies(self):
        self.reptiles.addSpecies('Gecko')
        result = self.reptiles.outSpecies()
        expected = ['Crocodile', 'Lizard', 'Snake', 'Turtle', 'Gecko']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
