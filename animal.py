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
        self.__feed = False
        self.__health = False

    def __eq__(self, other):
        if isinstance(other, Animal):
            return (self.name, self.species) == (other.name, other.species)
        return False

    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

    @property
    def age(self):
        return self.__age

    @property
    def dietary(self):
        return self.__dietary

    @property
    def animals(self):
        return self.__animals

    @property
    def feed(self):
        return self.__feed

    @feed.setter
    def feed(self, value):
        self.__feed = value

    def health(self):
        return self.__health

    def add_animals(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
            print(f"Added {animal.name} into {self.animals}")

        else:
            print(f"The {animal.name} already exists in {self.animals}")

    def remove_animals(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
            print(f"Added {animal.name} into {self.animals}")

        else:
            print(f"The {animal.name} already exists in {self.animals}")

    def assign_animal(self, animal):
        pass

    def animal_health(self, severity, notes, behavioural_concerns, date):
        return f"The severity is {severity}, the notes are {notes}, the behavioural_concerns are {behavioural_concerns}, the date is {date}"


    def health_reports(self):
        # TODO Record Health reports for individual animals or across the zoo
        # TODO It should influence zoo operations (e.g animals under treatment should not be moved or displayed)
        pass

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    def __str__(self):
        return "The animal is sleeping"


class Mammal(Animal):
    def __init__(self, name, species, age, dietary):
        super().__init__(name, species, age, dietary)

    def speak(self):
        return f"The {self.species} has spoken"

    def eat(self):
        return f"The {self.species} has ate"

    def sleep(self):
        return f"The {self.species} is sleeping"


class Reptile(Animal):
    def __init__(self, name, species, age, dietary):
        super().__init__(name, species, age, dietary)

    def speak(self):
        return f"The {self.species} has spoken"

    def eat(self):
        return f"The {self.species} has ate"

    def sleep(self):
        return f"The {self.species} is sleeping"


class Birds(Animal):
    def __init__(self, name, species, age, dietary):
        super().__init__(name, species, age, dietary)

    def speak(self):
        return f"The {self.species} has spoken"

    def eat(self):
        return f"The {self.species} has spoken"

    def sleep(self):
        return f"The {self.species} has spoken"
