"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod
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

    def feed_animal(self, animal):
        pass

    def clean_enclosure(self):
        pass

    def health_check(self):
        pass

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

class Veterinarian(Staff):
    def __init__(self, role, responsibilities):
        super().__init__(role, responsibilities)
