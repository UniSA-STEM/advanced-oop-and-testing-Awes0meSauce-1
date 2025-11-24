"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
import animal
from animal import Animal, Mammal
test = Mammal("test", "test", "test", "test")
a = Mammal("a", "a", "a", "a")

from abc import ABC, abstractmethod


class Enclosure(ABC):
    def __init__(self, size, environmental_type, cleanliness=False):
        self.__size = size
        self.__environmental_type = environmental_type
        self.__cleanliness = cleanliness
        self.__enclosures = []



    @property
    def size(self):
        return self.__size

    @property
    def environmental_type(self):
        return self.__environmental_type

    @property
    def cleanliness(self):
        return self.__cleanliness

    @property
    def enclosures(self):
        return self.__enclosures

    @cleanliness.setter
    def cleanliness(self, value):
        self.__cleanliness = value

    def check_type(self, animal: Animal):
        if animal not in self.enclosures:
           self.enclosures.append(animal)
           print(f"{animal.name} has joined {self.environmental_type}")
        else:
            print(f"{animal.name} has already joined {self.environmental_type}")

    def current_status(self):
        pass

    def list_of_animals(self):
        if not test.animals:
           return "There are no animals in this environment"
        else:
             for an in test.animals:
                 print(an.animal_name)
             return None

    def add_enclosure(self, enclosures):
        if enclosures not in self.enclosures:
            self.enclosures.append(enclosures)
            print(f"Added {enclosures.name} into {self.enclosures}")

        else:
            print(f"The {enclosures.name} already exists in {self.enclosures}")

    def remove_enclosure(self, enclosures):
        if enclosures not in self.enclosures:
            self.enclosures.append(enclosures)
            print(f"Added {enclosures.name} into {self.enclosures}")

        else:
            print(f"The {enclosures.name} already exists in {self.enclosures}")

    def daily_routines(self):
        pass

    def generate_report(self):
        return f"The enclosures in the zoo are {self.enclosures} \nThe environmental types are {self.environmental_type} \nThe cleanliness are {self.cleanliness} \nThe animals are {self.list_of_animals()}"
    def __str__(self):
        return f"The animal is sleeping, {self.enclosures}"

class Aquatic(Enclosure):
      def __init__(self, size, environmental_type, cleanliness):
          super().__init__(size, environmental_type, cleanliness)


class Savanna(Enclosure):
      def __init__(self, size, environmental_type, cleanliness):
          super().__init__(size, environmental_type, cleanliness)
