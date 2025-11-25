"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from enclosure import Enclosure, Aquatic, Savanna
from animal import Animal, Mammal, Reptile
from staff import Staff, Zookeeper, Veterinarian

savannah = Savanna("Savannah", 1, "Savanna", False)
aquatic = Aquatic("Aquatic", 1, "Aquatic", False)

leo = Mammal("Leo", "Lion", 6, "Meat")
dip = Reptile("Dip", "Fish", 6, "Grass")

jim = Zookeeper("Jim", 21, "Zookeeper", "Feeds Animals and Cleans the Enclosures")
bob = Veterinarian("Bob", 18, "Veterinarian", False)

