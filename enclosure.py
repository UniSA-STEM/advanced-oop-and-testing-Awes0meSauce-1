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
    def __init__(self, size, environmental_type, cleanliness=False):
        self.__size = size
        self.__environmental_type = environmental_type
        self.__cleanliness = cleanliness
        self.__enclosures = []
        self.__enclosure_id = 1

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

    @property
    def enclosure_id(self):
        return self.__enclosure_id

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

    def add_enclosure(self, animal: Animal):
        enclosure_record = self.enclosure_id, animal.name, animal.species, animal.age, animal.dietary
        self.enclosures.append(enclosure_record)
        print(f"Added {enclosure_record} \n Enclosure record: {self.enclosures}")
        self.enclosure_id += 1

    def remove_enclosure(self, id):
        for enclosure_record in self.enclosures:
            if enclosure_record[0] == id:
                self.enclosures.remove(enclosure_record)
                print(f"Removed {enclosure_record} \nUpdated list: {self.enclosures}")
                return self.enclosures

        print("The Enclosure record does not exist")

        return None

    def daily_routines(self):
        pass

    def generate_report(self):
        return f"The enclosures in the zoo are {self.enclosures} \nThe environmental types are {self.environmental_type} \nThe cleanliness are {self.cleanliness} \nThe animals are"
    def __str__(self):
        return f"The animal is sleeping, {self.enclosures}"

    @enclosure_id.setter
    def enclosure_id(self, value):
        self._enclosure_id = value


class Aquatic(Enclosure):
      def __init__(self, size, environmental_type, cleanliness):
          super().__init__(size, environmental_type, cleanliness)


class Savanna(Enclosure):
      def __init__(self, size, environmental_type, cleanliness):
          super().__init__(size, environmental_type, cleanliness)
