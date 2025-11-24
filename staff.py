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
    def __init__(self):
        self.__staff_record = []
        self.__health_record = []
        self.__id = 1
        self.__staff_id = 1

    @property
    def staff_record(self):
        return self.__staff_record

    @property
    def health_record(self):
        return self.__health_record

    @health_record.setter
    def health_record(self, value):
        self.__health_record = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def staff_id(self):
        return self.__staff_id

    @staff_id.setter
    def staff_id(self, value):
        self.__staff_id = value



    def add_staff(self, name, age, role, responsibilities):
        staff_record = [self.id, name, age, role, responsibilities]

        self.staff_record.append(staff_record)
        print(f"Added {staff_record} \n Staff record: {self.staff_record}")

        self.staff_id += 1

    def remove_staff(self, staff_id):
        for record in self.staff_record:
            if record[0] == staff_id:
                self.health_record.remove(record)
                print(f"Removed {record} \nUpdated list: {self.staff_record}")
                return self.staff_record

        print("The staff record does not exist")
        return None

    def __str__(self):
        return f"The staff are {self.staff_record}\n" f"The health records currently are {self.health_record}"

class Zookeeper(Staff):
    def __init__(self):
        super().__init__()

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

    def add_health_record(self, description, severity, notified, treatment_plan):

        health_record = [self.id, description, severity, notified, treatment_plan]

        self.health_record.append(health_record)
        print(f"Added {health_record} \n Health_record: {self.health_record}")

        self.id += 1

    def remove_health_record(self, id):
        for record in self.health_record:
            if record[0] == id:
               self.health_record.remove(record)
               print(f"Removed {record} \nUpdated list: {self.health_record}")
               return self.health_record

        print("The Health record does not exist")
        return None

    def __str__(self):
        parent_str = super().__str__()
        return parent_str


class Veterinarian(Staff):
    def __init__(self):
        super().__init__()

    def health_check(self, animals: Animal):
        if not animals.health:
           print(f"The {animals.name} is healthy now")
           animals.health = True
        else:
            print(f"The {animals.name} is already healthy")

    def __str__(self):
        parent_str = super().__str__()
        return parent_str

