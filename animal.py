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
    def __init__(self, name, species, age, dietary, feed=False, health=False):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary = dietary
        self.__feed = feed
        self.__health = health
        self.__animals = []
        self.__animal_health = []
        self.__feed = feed
        self.__health = health
        self.__animal_id = 1
        self.__severity = None
        self.__notes = None

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

    @property
    def animal_health(self):
        return self.__animal_health

    @property
    def animal_id(self):
        return self.__animal_id

    @animal_id.setter
    def animal_id(self, value):
        self._animal_id = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def severity(self):
        return self.__severity

    @severity.setter
    def severity(self, value):
        self.__severity = value

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value):
        self.__notes = value


    def assign_animal(self, animal):
        pass

    def animal_total_health(self, staff, severity, notes, behavioural_concerns, date):
        self.severity = severity
        self.notes = notes
        staff.animal_record = [self.animal_id, self.severity, self.notes, behavioural_concerns, date]
        self.animal_health.append(staff.animal_record)
        print(f"Added {staff.animal_record} \n Staff record: {self.animal_health}")
        self.animal_id += 1
        return f"The severity is {severity}, the notes are {notes}, the behavioural_concerns are {behavioural_concerns}, the date is {date}"

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
        return f"{self.name}, {self.species}, {self.age}, {self.dietary}, {self.feed}, {self.health} "

class Mammal(Animal):
    def __init__(self, name, species, age, dietary):
        super().__init__(name, species, age, dietary)

    def speak(self):
        return f"The {self.species} has howled at the other animal."

    def eat(self):
        return f"The {self.species} has ate all kinds of foods."

    def sleep(self):
        return f"The {self.species} is sleeping to save their energy."

    def __str__(self):
        parent_str = super().__str__()
        return parent_str


class Reptile(Animal):
    def __init__(self, name, species, age, dietary):
        super().__init__(name, species, age, dietary)

    def speak(self):
        return f"The {self.species} has hissed at the other animal."

    def eat(self):
        return f"The {self.species} has ate a insect."

    def sleep(self):
        return f"The {self.species} is sleeping to reduce stress."


class Birds(Animal):
    def __init__(self, name, species, age, dietary):
        super().__init__(name, species, age, dietary)

    def speak(self):
        return f"The {self.species} has spoken to the other animal in song."

    def eat(self):
        return f"The {self.species} has ate a fish."

    def sleep(self):
        return f"The {self.species} has puffed up it's feathers for insulation."
