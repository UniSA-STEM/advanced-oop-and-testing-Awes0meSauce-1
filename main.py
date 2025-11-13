"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from enclosure import Enclosure
from animal import Animal, Mammal

enclosure1 = Enclosure(1, "Aquatic", "Clean")
print(enclosure1)


mammal1 = Mammal("Mammal", "Mammal", 1, "Meat")
print(mammal1)
print(enclosure1.check_type(Mammal("Mammal", "Mammal", 1, "Meat")))
print(enclosure1)
print(enclosure1.check_type(Mammal("Mammal", "Mammal", 1, "Meat")))
print(enclosure1)

