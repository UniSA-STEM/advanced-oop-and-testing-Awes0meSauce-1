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
    __next_id = 1
    __total_records = []
    def __init__(self, name, size, environmental_type, cleanliness=False):
        self.__total_records = Enclosure.__total_records
        self.__id = Enclosure.__next_id
        Enclosure.__next_id += 1

        self.__name = name
        self.__size = size
        self.__environmental_type = environmental_type
        self.__cleanliness = cleanliness
        self.__animal_enclosures = []
        self.__enclosures = []
        self.__animal_enclosure_id = 1
        self.__enclosure_id = 1
        self.__staff_id = 1

    @property
    def id(self):
        return self.__id

    @property
    def total_records(self):
        return self.__total_records

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
    def enclosure_id(self):
        return self.__enclosure_id

    @property
    def staff_id(self):
        return self.__staff_id

    @property
    def enclosures(self):
        return self.__enclosures

    @enclosures.setter
    def enclosures(self, value):
        self.__enclosures = value

    def check_type(self, animal: Animal):
        for species in self.animal_enclosures:
            different_species = species[2]
            if different_species != animal.species:
               print("The type of animal is wrong")
               return True

        return False

    def daily_tasks(self, daily_tasks = list):
        for d in daily_tasks:
            print("Daily Task:", d)

    def list_of_animals(self):
        if not test.animals:
           return "There are no animals in this environment"
        else:
             for an in test.animals:
                 print(an.animal_name)
             return None

    def animal_assign_enclosure(self, animal: Animal):
        if self.check_type(animal):
           return

        animal_enclosure_record = self.animal_enclosure_id, animal.name, animal.species, animal.age, animal.dietary
        self.animal_enclosures.append(animal_enclosure_record)
        print(f"The Enclosure is {self.name}, it has added {animal_enclosure_record} \nEnclosure {self.name} record: {self.animal_enclosures}")
        self.animal_enclosure_id += 1

    def animal_design_enclosure(self, id):
        for enclosure_record in self.animal_enclosures:
            if enclosure_record[0] == id:
                self.animal_enclosures.remove(enclosure_record)
                print(f"Removed {enclosure_record} \nUpdated list: {self.animal_enclosures}")
                return self.animal_enclosures

        print("The Enclosure record does not exist")
        return None


    @abstractmethod
    def generate_report(self):
        pass

    def __str__(self):
        return f"{self.name}, {self.size}, {self.environmental_type}, {self.cleanliness}"

    @staff_id.setter
    def staff_id(self, value):
        self._staff_id = value


class Aquatic(Enclosure):
      def __init__(self, name, size, environmental_type, cleanliness):
          super().__init__(name, size, environmental_type, cleanliness)

      def generate_report(self):
          enclosure_record = self.id, self.name, self.size, self.environmental_type, self.cleanliness
          self.total_records.append(enclosure_record)
          print(f"Added {enclosure_record} \nEnclosure record: {self.total_records}")
          return enclosure_record


class Savanna(Enclosure):
      def __init__(self, name, size, environmental_type, cleanliness):
          super().__init__(name, size, environmental_type, cleanliness)

      def generate_report(self):
          enclosure_record = self.id, self.name, self.size, self.environmental_type, self.cleanliness
          self.total_records.append(enclosure_record)
          print(f"Added {enclosure_record} \nEnclosure record: {self.total_records}")
          return enclosure_record
