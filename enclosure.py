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

    def get_size(self):
        return self.__size

    def get_environmental_type(self):
        return self.__environmental_type

    def get_cleanliness(self):
        return self.__cleanliness

    def check_type(self):
        pass

    def current_status(self):
        pass

    def list_of_animals(self):
        pass

    def add_enclosure(self):
        pass

    def remove_enclosure(self):
        pass

    def daily_routines(self):
        pass

    def generate_report(self):
    #TODO Generate lists of animals by species
    #TODO Generate status of enclosures


    def __str__(self):
        return "The animal is sleeping"