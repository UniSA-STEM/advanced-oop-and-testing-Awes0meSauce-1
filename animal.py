"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, species, age, dietary):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary = dietary
        self.__animals = []

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_dietary(self):
        return self.__dietary

    def get_animals(self):
        return self.__animals

    @abstractmethod
    def speak(self):
        pass

    def add_animals(self, animal):
        self.get_animals().append(animal)

    def remove_animals(self, animal):
        for animal in animal.get_animals():
            if animal in self.get_animals():
                self.__animals.append(animal)
            else:
                print("Animal is not present in the animals list")

    def assign_animal(self, animal):
        pass

    def animal_health(self):
    #TODO Record health issues such as injuries, illness, or behavioural concerns
    #TODO Record relevant details including a descriptions of the issue, the date is reported
    #TODO Record the severity level, any treatment plans or notes
        pass

    def health_reports(self):
    #TODO Record Health reports for individual animals or across the zoo
    #TODO It should influence zoo operations (e.g animals under treatment should not be moved or displayed)
        pass

    def __str__(self):
        return "The animal is sleeping"


class Mammal(Animal):
    def __init__(self, name, species, age, dietary):
        super().__init__(name, species, age, dietary)

    def speak(self):
        return "Bark"

class Reptile(Animal):
    def __init__(self, name, species, age, dietary):
        super().__init__(name, species, age, dietary)

class Birds(Animal):
    def __init__(self, name, species, age, dietary):
        super().__init__(name, species, age, dietary)