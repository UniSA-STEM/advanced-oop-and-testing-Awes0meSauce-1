"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from enclosure import Enclosure, Aquatic, Savanna
from animal import Animal, Mammal
from staff import Staff, Zookeeper

savannah = Savanna(1, "Savanna", "Clean")

leo = Mammal("Leo", "Lion", 6, "Meat")
savannah.add_enclosure(leo)
print(leo)

zookeeper1 = Zookeeper()
zookeeper1.add_staff("Jim", 21, "Zookeeper", "Feeds Animals and Cleans the Enclosures" )

savannah.generate_report()
leo.animal_total_health("Light", "There is a slight bruise on the right arm.", "There are no behavioural concerns", "9th of November")
print(savannah)
zookeeper1.add_health_record("a", "a", "a", "a")
zookeeper1.add_health_record("b", "b", "b", "b")
zookeeper1.remove_health_record(1)
print(zookeeper1)

