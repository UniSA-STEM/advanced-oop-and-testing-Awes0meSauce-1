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
savannah.assign_enclosure(leo)
savannah.assign_enclosure(dip)
aquatic.assign_enclosure(dip)
savannah.generate_report()
aquatic.generate_report()

jim = Zookeeper("Jim", 21, "Zookeeper", "Feeds Animals and Cleans the Enclosures")
bob = Veterinarian("Bob", 18, "Veterinarian", False)
jim.add_staff()
jim.clean_enclosure(savannah)
print(savannah)
print(aquatic)
jim.feed_animal(leo)
bob.health_check(leo)
print(leo)
# leo.animal_total_health("Light", "There is a slight bruise on the right arm.", "There are no behavioural concerns", "9th of November")
# print(savannah)
# jim.add_health_record("a", "a", "a", "a")
# jim.add_health_record("b", "b", "b", "b")
# jim.remove_health_record(1)
# print(jim)

