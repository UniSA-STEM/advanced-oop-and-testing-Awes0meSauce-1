"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

import animal
from animal import Animal
from enclosure import Enclosure


class Staff(ABC):
    def __init__(self, role, responsibilities):
        self.__role = role
        self.__responsibilities = responsibilities
        self.__staff = []

    @property
    def role(self):
        return self.__role

    @property
    def responsibilities(self):
        return self.__responsibilities

    @property
    def staff(self):
        return self.__staff

    def add_staff(self, staff):
        if staff not in self.staff:
            self.staff.append(staff)
            print(f"Added {staff.name} into {self.staff}")

        else:
            print(f"The {staff.name} already exists in {self.staff}")

    def remove_staff(self, staff):
        if staff not in self.staff:
            self.staff.append(staff)
            print(f"Added {staff.name} into {self.staff}")

        else:
            print(f"The {staff.name} already exists in {self.staff}")

class Zookeeper(Staff):
    def __init__(self, role, responsibilities):
        super().__init__(role, responsibilities)

    def feed_animal(self, animals: Animal):
        if animals.feed is False:
           print(f" The {animals.name} has been feed")
           animals.feed = True
        else:
            print(f" The {animals.name} has already been feed")

    def clean_enclosure(self, enclosure: Enclosure):
        if enclosure.cleanliness is False:
           print(f" The {enclosure.cleanliness} has been cleaned")
           enclosure.cleanliness = True
        else:
            print(f" The {enclosure.cleanliness} has already been cleaned")

class Veterinarian(Staff):
    def __init__(self, role, responsibilities):
        super().__init__(role, responsibilities)

    def health_check(self, animals: Animal):
        if not animals.health:
           print(f"The {animals.name} is healthy now")
           animals.health = True
        else:
            print(f"The {animals.name} is already healthy")

