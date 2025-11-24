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
from staff import Staff, Zookeeper

enclosure1 = Enclosure(1, "Aquatic", "Clean")
print(enclosure1)


mammal1 = Mammal("Mammal", "Mammal", 1, "Meat")
print(mammal1)
print(enclosure1.check_type(Mammal("Mammal", "Mammal", 1, "Meat")))
print(enclosure1)
print(enclosure1.check_type(Mammal("Mammal", "Mammal", 1, "Meat")))
print(enclosure1)

staff1 = Staff("Staff", "Staff")
zookeeper1 = Zookeeper("Zookeeper", "Zookeeper")
print(zookeeper1.feed_animal(Mammal("Mammal", "Mammal", 1, "Meat")))

mammal1.add_animals(mammal1)
print(enclosure1.list_of_animals())
print(enclosure1.generate_report())
print(mammal1.animal_health("Light", "There is a slight bruise on the right arm.", "There are no behavioural concerns", "9th of November"))
zookeeper1.add_health_record("a", "a", "a", "a")
zookeeper1.add_health_record("b", "b", "b", "b")
zookeeper1.remove_health_record(1)
print(zookeeper1)

