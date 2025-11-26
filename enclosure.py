"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

from exception import EnclosureFullException, SingleSpeciesException, IDEnclosureException
from animal import Animal


class Enclosure(ABC):
    __next_id = 1
    __total_records = []

    def __init__(self, name, size, environmental_type, cleanliness=False):
        self.__total_records = Enclosure.__total_records
        self.__id = Enclosure.__next_id
        Enclosure.__next_id += 1

        self.__name = name
        self.__size = size
        self.__environmental_type = environmental_type
        self.__cleanliness = cleanliness
        self.__animal_enclosures = []
        self.__enclosures = []
        self.__animal_enclosure_id = 1
        self.__enclosure_id = 1
        self.__staff_id = 1

    # This is the getter from self.__id
    @property
    def id(self):
        return self.__id

    # This is the getter from self.total_records
    @property
    def total_records(self):
        return self.__total_records

    # This is the getter from self.__name
    @property
    def name(self):
        return self.__name

    # This is the getter from self.__size
    @property
    def size(self):
        return self.__size

    # This is the getter from self.__environmental_type
    @property
    def environmental_type(self):
        return self.__environmental_type

    # This is the getter from self.__cleanliness
    @property
    def cleanliness(self):
        return self.__cleanliness

    # This is the getter from self.__animal_enclosures
    @property
    def animal_enclosures(self):
        return self.__animal_enclosures

    # This is the setter from self.__cleanliness
    @cleanliness.setter
    def cleanliness(self, value):
        self.__cleanliness = value

    # This is the getter from self.__animal_enclosure_id
    @property
    def animal_enclosure_id(self):
        return self.__animal_enclosure_id

    # This is the setter from self.__animal_enclosure_id
    @animal_enclosure_id.setter
    def animal_enclosure_id(self, value):
        self.__animal_enclosure_id = value

    # This is the getter from self__enclosure_id
    @property
    def enclosure_id(self):
        return self.__enclosure_id

    # This is the getter from self.__staff_id
    @property
    def staff_id(self):
        return self.__staff_id

    # This is the setter from self.__staff_id
    @staff_id.setter
    def staff_id(self, value):
        self.__staff_id = value

    # This is the getter from self.__enclosures
    @property
    def enclosures(self):
        return self.__enclosures

    # This is the setter from self.__enclosures
    @enclosures.setter
    def enclosures(self, value):
        self.__enclosures = value

    # This will check for the type of animal using the animal: Animal method.
    def check_type(self, animal: Animal):
        # It will loop through all the animal_enclosures and will record each animal in the enclosure in the species
        # method.
        for species in self.animal_enclosures:
            # Then it will grab the species by grabbing the 2nd item list which is actually the 3rd due to how item lists
            # work, and then it will assign it to the different_species method.
            different_species = species[2]
            # Then if the "different_species" is not equal to the animal species it will print an output below
            try:
                if different_species != animal.species:
                   # Said output
                   raise SingleSpeciesException(
                   f"{different_species} is the only species. Cannot add {animal.species}")

                return False

            except SingleSpeciesException as e:
                print(e)
                return True
        return None

    # This will check the size of the enclosure and if the animals exceed the size of the enclosure it will return true
    # if not it will return false
    def check_size(self, animal):
        # This will make the new method "maximum_size = the current size of the enclosure
        maximum_size = self.size
        # Then it will make the new method "current_animals" into the length of the enclosure which in this case
        # would be how many animals there are
        current_animals = len(self.animal_enclosures)
        # Then it will check if the current animals in the enclosure is greater or equal to the maximum size of the enclosure
        try:
            if current_animals >= maximum_size:
                # If it is it will print out this output
                raise EnclosureFullException(
                    f"{self.name} is full (Capacity {self.size}). Cannot add {animal.name}."
                )

            # And returning a value of this being false.
            return False

        except EnclosureFullException as e:
            print(e)
            return True

    # Using a list as the daily_tasks this will print the daily_tasks needed while also being an output for different
    # functions and calls
    def daily_tasks(self, daily_tasks=list):
        for d in daily_tasks:
            print("Daily Task:", d)

    # This function will assign an animal to an enclosure using the animal: Animal method, it will first check
    # for the self.check_type function then the self.check_size function then if that all passes correctly
    # it will assign the animal to the enclosure
    def animal_assign_enclosure(self, animal: Animal):
        # Checking the check_type function
        if self.check_type(animal):
            return

        # Checking the check_size function
        if self.check_size(animal):
            return

        # This will set the animal enclosures id, the animals name, the species of the animal, the age of the animal
        # and the dietary of the animal to animal enclosure record
        animal_enclosure_record = self.animal_enclosure_id, animal.name, animal.species, animal.age, animal.dietary
        # Then it will append all of that into the animal_enclosures list using the append function
        self.animal_enclosures.append(animal_enclosure_record)
        # Then it will print an output
        print(
            f"The Enclosure is {self.name}, it has added {animal_enclosure_record} \nEnclosure {self.name} record: {self.animal_enclosures}")
        # An increase the id to each animal in the enclosure so each animal in the enclosure has a different id
        self.animal_enclosure_id += 1

    # This will do the opposite of the animal_assign enclosure by instead of assigning an animal to an enclosure
    # it will design an animal to an enclosure by using the id to check which animal needs designing to the enclosure
    def animal_design_enclosure(self, id):
        # This will loop through all the animals in the enclosure
        try:
            for enclosure_record in self.animal_enclosures:
            # Then checking the id in the enclosure is equal to the id requested
                if enclosure_record[0] == id:
                   # It wil remove the specific enclosure desired
                   self.animal_enclosures.remove(enclosure_record)
                   # And print an output.
                   print(f"Removed {enclosure_record} \nUpdated list: {self.animal_enclosures}")
                   return self.animal_enclosures

        # If the id is not in the list of animals in the enclosure it will post this.
            raise IDEnclosureException(f"Enclosure record with ID: {id} does not exist.")

        except IDEnclosureException as e:
            print(e)
            return None
    # This will move an animal to an different enclosure by inputting the old_enclosure the animal is
    # currently in and the new enclosure also importing the animal class using animal: Animal
    def animal_move_enclosure(self, id, animal: Animal, old_enclosure, new_enclosure):

        # This will check the type of the animal
        if self.check_type(animal):
            return

        # Then it will check the size of the enclosure
        if self.check_size(animal):
            return

        # Then it will check if the animal has been treated or not
        if animal.animal_treatment():
            return

        # Then it will pass the old_enclosure and the id into the animal_design_enclosure function
        old_enclosure.animal_design_enclosure(id)
        # Then it will pass the new_enclosure along with the animal to the animal_assign_enclosure function
        new_enclosure.animal_assign_enclosure(animal)

    # This is an abstractmethod so it will be passed to the children classes
    @abstractmethod
    def generate_report(self):
        pass

    def __str__(self):
        return f"{self.name}, {self.size}, {self.environmental_type}, {self.cleanliness}"


class Aquatic(Enclosure):
    def __init__(self, name, size, environmental_type, cleanliness):
        super().__init__(name, size, environmental_type, cleanliness)

    # Using the abstract method above this will generate a report showing the id of the enclosure, the name of the enclosure
    # the size of the enclosure, the environmental type of the enclosure and the cleanliness of the enclosure
    def generate_report(self):
        enclosure_record = (f"ID: {self.id}, "
                            f"Name: {self.name}, "
                            f"Size: {self.size}, "
                            f"Environmental Type: {self.environmental_type}, "
                            f"Cleanliness: {self.cleanliness}")
        # This will append it to the total records so all enclosures can be shown at once
        self.total_records.append(enclosure_record)
        # Then it will print an output
        print(f"Added {enclosure_record} \nEnclosure record: {self.total_records}")
        return enclosure_record


class Savanna(Enclosure):
    def __init__(self, name, size, environmental_type, cleanliness):
        super().__init__(name, size, environmental_type, cleanliness)

    # This will do the same as the generate report in the Aquatic section because it is an abstract method it needs the
    # function here.
    def generate_report(self):
        enclosure_record = (f"ID: {self.id}, "
                            f"Name: {self.name}, "
                            f"Size: {self.size}, "
                            f"Environmental Type: {self.environmental_type}, "
                            f"Cleanliness: {self.cleanliness}")
        self.total_records.append(enclosure_record)
        print(f"Added {enclosure_record} \nEnclosure record: {self.total_records}")
        return enclosure_record
