"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal


class Enclosure:
    def __init__(self, size, environmental_type, cleanliness):
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

    def check_type(self):
        pass

    def current_status(self):
        pass

    def list_of_animals(self):
        pass

    def add_enclosure(self):
        self.enclosures.append(Enclosure(self.__size, self.__environmental_type, self.__cleanliness))

    def remove_enclosure(self, enclosure):
        for enclosure in self.enclosures:
            if enclosure in self.enclosures:
                self.enclosures.append(enclosure)
            else:
                print("Enclosures is not present in the enclosure list")

    def daily_routines(self):
        pass

    def generate_report(self):
    #TODO Generate lists of animals by species
    #TODO Generate status of enclosures
        pass


    def __str__(self):
       return "The animal is sleeping"