"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod
from animal import Animal
from enclosure import Enclosure
from exception import AnimalFullException, EnclosureCleanedException, UnsufficientHealthRecordException, \
    InsufficientSeverityException


class Staff(ABC):
    def __init__(self, name, age, role, responsibilities):
        self.__name = name
        self.__age = age
        self.__role = role
        self.__responsibilities = responsibilities
        self.__staff_record = []
        self.__health_record = []
        self.__id = 1
        self.__staff_id = 1

    # Is the getter of the method (name)
    @property
    def name(self):
        return self.__name

    # Is the getter of the method (age)
    @property
    def age(self):
        return self.__age

    # Is the getter of the method (role)
    @property
    def role(self):
        return self.__role

    # Is the getter of the method (responsibilities)
    @property
    def responsibilities(self):
        return self.__responsibilities

    # Is the getter of the method (staff record)
    @property
    def staff_record(self):
        return self.__staff_record

    # Is the getter of the method (health record)
    @property
    def health_record(self):
        return self.__health_record

    # Is the setter of the method (health record)
    @health_record.setter
    def health_record(self, value):
        self.__health_record = value

    # Is the getter of the method (id)
    @property
    def id(self):
        return self.__id

    # Is the setter of the method (id)
    @id.setter
    def id(self, value):
        self.__id = value

    # Is the getter of the method (staff id)
    @property
    def staff_id(self):
        return self.__staff_id

    # Is the setter of the method (staff id)
    @staff_id.setter
    def staff_id(self, value):
        self.__staff_id = value

        # This function will assign a staff member to an enclosure of the desired type using the (enclosure: Enclosure) method

    def staff_assign_enclosure(self, enclosure: Enclosure):
        # Using the staff enclosure record method it will assign, the enclosure staff_id, the enclosures name,
        # the enclosures age, the enclosures role and the enclosures responsibilities to the method
        staff_enclosure_record = enclosure.staff_id, self.name, self.age, self.role, self.responsibilities

        # Then it will append the method above to the enclosures animal_enclosure list
        enclosure.animal_enclosures.append(staff_enclosure_record)

        # Then it will print the output below.
        print(
            f"The Enclosure is {enclosure.name}, it has added {staff_enclosure_record} \nEnclosure {enclosure.name} record: {enclosure.animal_enclosures}")

        # Then it will increase the staff id so each staff will have a different id
        self.staff_id += 1

        return None

    def __str__(self):
        return f"The staff are {self.staff_record}\n" f"The health records currently are {self.health_record}"


class Zookeeper(Staff):
    def __init__(self, name, age, role, responsibilities):

        # This will return the parent class being staff into the children's class being (Zookeeper)
        super().__init__(name, age, role, responsibilities)

    # This will check if the animal has been feed, if the animal has not been feed it will print and output and
    # change the "animals" feed to True
    def feed_animal(self, animals: Animal):
        # Checking if the animals feed is False
        try:
            if animals.feed is False:
                # Printing an output
                print(f"{animals.name} has been feed")
                # Changing the value to true
                animals.feed = True

            #If it has already been fed it will produce this output
            else:
                raise AnimalFullException(f"{animals.name} has already been feed")
        except AnimalFullException as e:
            print(e)
            return f"The animal {animals.name} fed level is {animals.feed}"

    # This will check if the enclosure has been cleaned using the enclosure: Enclosure method
    # if the enclosure cleanliness is False it will produce an output and change the enclosure cleanliness
    # to true
    def clean_enclosure(self, enclosure: Enclosure):
        # Checking if the enclosure cleanliness is false
        try:
            if enclosure.cleanliness is False:
                # Printing an output
                print(f"The {enclosure.name} has been cleaned")
                # Changing the enclosure cleanliness to true
                enclosure.cleanliness = True

                # If it's already cleaned it will print an output saying it's already been cleaned
            else:
                raise EnclosureCleanedException(f"The {enclosure.name} has already been cleaned")

        except EnclosureCleanedException as e:
            print(e)

    # This will add a health record checking what animal it is using the animal: Animal method, checking if it's notified
    # using the notified method and check what treatment_plan the animal has or hasn't been applied to the animal.
    def add_health_record(self, animal: Animal, notified, treatment_plan):

        # This will assign the severity of the animal, the notes of the animal if it's been notified and the
        # treatment plan to the method (health_record)
        health_record = [self.id, animal.severity, animal.notes, notified, treatment_plan]

        # Then it will append it to a self version of the health record
        self.health_record.append(health_record)
        print(f"Added {health_record} \nHealth_record: {self.health_record}")

        # It will increase the id so each record will have a different id.
        self.id += 1

    # Basically this will do the opposite of the add health record function and instead of adding a health record
    # it will remove a health_record using the id as a base to check which one it needs to remove.
    def remove_health_record(self, id):
        # Using a for loop it will loop through all the records
        for record in self.health_record:
            # This will check if the "record" value is equal to the id to see if it's the desired record
            # that needs removing
            try:
                if record[0] == id:
                # Then it will remove said record
                   self.health_record.remove(record)
                   # And print an output because of it
                   print(f"Removed {record} \nUpdated list: {self.health_record}")

                   # Then returning the updated health records
                   return self.health_record

           # If the health record doesn't exist it will print this output
                else:
                    raise UnsufficientHealthRecordException("The Health record does not exist")
            except AnimalFullException as e:
                  print(e)
                  return None
        return None

    # Then it will be able to return the parent's string into the children string
    def __str__(self):
        parent_str = super().__str__()
        return parent_str


class Veterinarian(Staff):
    # This will return the parents __init__ function into the children __init__ function
    def __init__(self, name, age, role, responsibilities):
        super().__init__(name, age, role, responsibilities)

    # This will check the health of the animal using the animal: Animal method
    def health_check(self, animal: Animal):
        # This will check for the severity of the animal being Low, Medium, High or Very High
        severity = ["Low", "Medium", "High", "Very High"]
        # This will loop using a for loop of the severity above.
        for s in severity:
            # Then it will check if the animal severity matches
            try:
                if animal.severity == s:
                # Then it will set the animals health to False because it has some kind of injury
                   animal.health = False
                # Then printing an output to match the method above
                   print(f"{animal.name} {animal.health}")
                   return animal.health

            # Otherwise if the animal isn't injured in some way it will return the animals health to true
                elif animal.severity == "None":
                # Setting the animals health here
                     animal.health = True
                # And printing an output here
                     print(f"{animal.name} {animal.health}")
                     return animal.health

            # Otherwise if the severity in this function isn't one of the values mentioned above it will tell the user to input
            # a correct severity.
                else:
                     raise InsufficientSeverityException(
                     f"The {animal.severity} is not a valid severity please choose from" "['None' 'Low', 'Medium', 'High', 'Very High']")
            except InsufficientSeverityException as e:
                   print(e)
                   return animal.health

    # Returning the parents string to the children string
    def __str__(self):
        parent_str = super().__str__()
        return parent_str
