import pytest

from animal import Animal, Mammal, Reptile, Birds
from main import leo


class TestAnimal:

    @pytest.fixture
    def sample_animal(self):
        return Mammal("Leo", "Lion", 6, "Meat")

    @pytest.fixture
    def sample_animal_health(self):
        leo.animal_total_health(leo, "Low", "Has a small cut on the right arm", "None", "9th of November")
        return leo.severity,leo.notes, leo.behavioural_concerns, leo.date

    @pytest.fixture
    def sample_inheritance_reptile(self):
        return Reptile("Reptile", "Reptile", 6, "Meat")

    @pytest.fixture
    def sample_inheritance_birds(self):
        return Birds("Birds", "Birds", 6, "Birds")

    def test_animal(self, sample_animal):
        assert sample_animal.name == "Leo"
        assert sample_animal.species == "Lion"
        assert sample_animal.age == 6
        assert sample_animal.dietary == "Meat"

    def test_animal2(self, sample_animal):
        assert sample_animal.animal_treatment() == False

    def test_animal3(self, sample_animal_health):
        assert leo.severity == "Low"
        assert leo.notes == "Has a small cut on the right arm"
        assert leo.behavioural_concerns == "None"
        assert leo.date == "9th of November"

    def test_animal4(self, sample_inheritance_reptile):
        assert sample_inheritance_reptile.speak() == "The Reptile has hissed at the other animal."

    def test_animal5(self, sample_inheritance_birds):
        assert sample_inheritance_birds.speak() == "The Birds has spoken to the other animal in song."

    def test_animal6(self, sample_animal):
        assert sample_animal.speak() == "The Lion has howled at the other animal."
