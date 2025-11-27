"""
File: main.py
Description: This is the main file where all the main commands are run, this file will do most of the calling
as none of the other files would work without it.
Author: Jack Gallagher
ID: 110410979
Username: galjh002
This is my own work as defined by the University's Academic Integrity Policy.
"""

from enclosure import Enclosure, Aquatic, Savanna
from animal import Animal, Mammal, Reptile
from staff import Staff, Zookeeper, Veterinarian

savannah = Savanna("Savannah", 1, "Savanna", False)
savannah2 = Savanna("Savannah2", 1, "Savanna", False)
aquatic = Aquatic("Aquatic", 1, "Aquatic", False)

leo = Mammal("Leo", "Lion", 6, "Meat")
butter = Mammal("Butter", "Lion", 7, "Meat")
dip = Reptile("Dip", "Fish", 6, "Grass")

jim = Zookeeper("Jim", 21, "Zookeeper", "Feeds Animals and Cleans the Enclosures")
bob = Veterinarian("Bob", 18, "Veterinarian", False)

savannah.animal_assign_enclosure(leo)
savannah.animal_assign_enclosure(dip)
savannah.animal_design_enclosure(999)
savannah.check_type(leo)
jim.feed_animal(leo)
jim.feed_animal(leo)
savannah2.animal_move_enclosure(1, leo, savannah, savannah2)
savannah.generate_report()
jim.staff_assign_enclosure(savannah)
savannah.daily_tasks([jim.feed_animal(leo)])
jim.clean_enclosure(savannah)
leo.animal_total_health(leo, "Low", "Has a small cut on the right arm", "None", "9th of November")
bob.health_check(leo)