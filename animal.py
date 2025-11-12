"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Animal:
    def __init__(self, name, species, age, dietary):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary = dietary

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_dietary(self):
        return self.__dietary

    def __str__(self):
        return "The animal is sleeping"


class Mammal(Animal):
    def __init__(self, name, species, age, dietary):
        super.__init__()

class Reptile(Animal):
    def __init__(self, name, species, age, dietary):
        super.__init__()

class Birds(Animal):
    def __init__(self, name, species, age, dietary):
        super.__init__()