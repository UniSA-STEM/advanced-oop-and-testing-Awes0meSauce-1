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

from abc import ABC, abstractmethod


class Enclosure(ABC):
    def __init__(self, name, size, environmental_type, cleanliness=False):
        self.__name = name
        self.__size = size
        self.__environmental_type = environmental_type
        self.__cleanliness = cleanliness
        self.__animal_enclosures = []
        self.__enclosures = []
        self.__animal_enclosure_id = 1
        self.__enclosure_id = 1

    @property
    def name(self):
        return self.__name

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
    def animal_enclosures(self):
        return self.__animal_enclosures

    @cleanliness.setter
    def cleanliness(self, value):
        self.__cleanliness = value

    @property
    def animal_enclosure_id(self):
        return self.__animal_enclosure_id

    @animal_enclosure_id.setter
    def animal_enclosure_id(self, value):
        self.__animal_enclosure_id = value

    @property
    def enclosures(self):
        return self.__enclosures

    @enclosures.setter
    def enclosures(self, value):
        self.__enclosures = value

    @property
    def enclosure_id(self):
        return self.__enclosure_id

    def check_type(self, animal: Animal):
        if animal not in self.animal_enclosures:
           self.animal_enclosures.append(animal)
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

    def assign_enclosure(self, animal: Animal):
        animal_enclosure_record = self.animal_enclosure_id, animal.name, animal.species, animal.age, animal.dietary
        self.animal_enclosures.append(animal_enclosure_record)
        print(f"Added {animal_enclosure_record} \n Enclosure record: {self.animal_enclosures}")
        self.animal_enclosure_id += 1

    def design_enclosure(self, id):
        for enclosure_record in self.animal_enclosures:
            if enclosure_record[0] == id:
                self.animal_enclosures.remove(enclosure_record)
                print(f"Removed {enclosure_record} \nUpdated list: {self.animal_enclosures}")
                return self.animal_enclosures

        print("The Enclosure record does not exist")

        return None

    def daily_routines(self):
        pass

    def generate_report(self):
        enclosure_record = self.enclosure_id, self.name, self.size, self.environmental_type, self.cleanliness
        self.enclosures.append(enclosure_record)
        print(f"Added {enclosure_record} \nEnclosure record: {self.enclosures}")
        self.animal_enclosure_id += 1
    def __str__(self):
        return f"The animal is sleeping, {self.enclosures}"

class Aquatic(Enclosure):
      def __init__(self, name, size, environmental_type, cleanliness):
          super().__init__(name, size, environmental_type, cleanliness)


class Savanna(Enclosure):
      def __init__(self, name, size, environmental_type, cleanliness):
          super().__init__(name, size, environmental_type, cleanliness)
