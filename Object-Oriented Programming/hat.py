import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

hat = Hat()
hat.sort("Harry")

#second version

import random

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

def sort(name):
    print(name, "is in", random.choice(houses))


sort("Harry")