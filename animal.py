"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

from exception import AnimalFullException


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
        self.__animal_id = 1
        self.__severity = None
        self.__notes = None

    # Is the getter of method (self.__name)
    @property
    def name(self):
        return self.__name

    # Is the getter of method (self.__species)
    @property
    def species(self):
        return self.__species

    # Is the getter of method (self.__age)
    @property
    def age(self):
        return self.__age

    # Is the getter of method (self.__dietary)
    @property
    def dietary(self):
        return self.__dietary

    # Is the getter of method (self.__animals)
    @property
    def animals(self):
        return self.__animals

    # Is the getter of method (self.__feed)
    @property
    def feed(self):
        return self.__feed

    # Is the setter of method (self.__feed)
    @feed.setter
    def feed(self, value):
        self.__feed = value

    # Is the getter of method (self.__animal_health)
    @property
    def animal_health(self):
        return self.__animal_health

    # Is the getter of method (self.__animal_id)
    @property
    def animal_id(self):
        return self.__animal_id

    # Is the setter of method (self.__animal_id)
    @animal_id.setter
    def animal_id(self, value):
        self.__animal_id = value

    # Is the getter of method (self.__health)
    @property
    def health(self):
        return self.__health

    # Is the setter of method (self.__health)
    @health.setter
    def health(self, value):
        self.__health = value

    # Is the getter of method (self.__severity)
    @property
    def severity(self):
        return self.__severity

    # Is the setter of method (self.__severity)
    @severity.setter
    def severity(self, value):
        self.__severity = value

    # Is the getter of method (self.__notes)
    @property
    def notes(self):
        return self.__notes

    # Is the setter of method (self.__notes)
    @notes.setter
    def notes(self, value):
        self.__notes = value

    # Importing the staff, severity notes behavioural concerns and date this will allow this function to generate a report
    # of the animals_total_health.
    def animal_total_health(self, staff, severity, notes, behavioural_concerns, date):
        # This allows severity and notes to be passed on the report without having being repeated in the report function
        self.severity = severity
        self.notes = notes
        # This allows to store the animal_id of the animal the severity, notes, behavioural_concerns and the date
        staff.animal_record = [self.animal_id, self.severity, self.notes, behavioural_concerns, date]
        # Then it will append all that into another list so it can be used for later
        self.animal_health.append(staff.animal_record)
        # Then it will print an output as so
        print(f"Added {staff.animal_record} \n Staff record: {self.animal_health}")
        # To have each animal_report accessible this is incremented when used by 1.
        self.animal_id += 1
        return f"The severity is {severity}, the notes are {notes}, the behavioural_concerns are {behavioural_concerns}, the date is {date}"

    # This will check if the animal is being treated because if the self.health method is equal to false it will
    # return the function as true otherwise it will return as false.
    def animal_treatment(self):
        if not self.health:
           print("This animal can't be moved since it's being treated")
           return True
        return False

    # This is an abstract method (speak) and will be passed on to the children class
    @abstractmethod
    def speak(self):
        pass

    # This is an abstract method (eat) and will be passed on to the children class
    @abstractmethod
    def eat(self):
        pass

    # This is an abstract method (sleep) and will be passed on to the children class
    @abstractmethod
    def sleep(self):
        pass

    def __str__(self):
        return f"{self.name}, {self.species}, {self.age}, {self.dietary}, {self.feed}, {self.health} "

class Mammal(Animal):
    def __init__(self, name, species, age, dietary):
        super().__init__(name, species, age, dietary)

    # This being the children class of Animal is the speak class for the children class (Mammal)
    def speak(self):
        return f"The {self.species} has howled at the other animal."

    # This being the children class of Animal is the eat class for the children class (Mammal)
    def eat(self):
        return f"The {self.species} has ate all kinds of foods."

    # This being the children class of Animal is the sleep class for the children class (Mammal)
    def sleep(self):
        return f"The {self.species} is sleeping to save their energy."

    def __str__(self):
        parent_str = super().__str__()
        return parent_str


class Reptile(Animal):
    def __init__(self, name, species, age, dietary):
        super().__init__(name, species, age, dietary)

    # This being the children class of Animal is the speak class for the children class (Reptile)
    def speak(self):
        return f"The {self.species} has hissed at the other animal."

    # This being the children class of Animal is the eat class for the children class (Reptile)
    def eat(self):
        return f"The {self.species} has ate a insect."

    # This being the children class of Animal is the sleep class for the children class (Reptile)
    def sleep(self):
        return f"The {self.species} is sleeping to reduce stress."


class Birds(Animal):
    def __init__(self, name, species, age, dietary):
        super().__init__(name, species, age, dietary)

    # This being the children class of Animal is the speak class for the children class (Birds)
    def speak(self):
        return f"The {self.species} has spoken to the other animal in song."

    # This being the children class of Animal is the eat class for the children class (Birds)
    def eat(self):
        return f"The {self.species} has ate a fish."

    # This being the children class of Animal is the sleep class for the children class (Birds)
    def sleep(self):
        return f"The {self.species} has puffed up it's feathers for insulation."
