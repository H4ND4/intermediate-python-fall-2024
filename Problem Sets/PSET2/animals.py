
class Mammals:
    def __init__(self):
        self.species = ['Lion', 'Elephant', 'Tiger', 'Bear']

    def outSpecies(self):
        return self.species

    def addSpecies(self, new_species):
        self.species.append(new_species)

class Birds:
    def __init__(self):
        self.species = ['Eagle', 'Parrot', 'Penguin', 'Owl']

    def outSpecies(self):
        return self.species

    def addSpecies(self, new_species):
        self.species.append(new_species)

class Reptiles:
    def __init__(self):
        self.species = ['Crocodile', 'Lizard', 'Snake', 'Turtle']

    def outSpecies(self):
        return self.species

    def addSpecies(self, new_species):
        self.species.append(new_species)
