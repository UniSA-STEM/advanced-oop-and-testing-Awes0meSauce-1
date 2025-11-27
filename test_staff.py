import pytest

from animal import Mammal
from enclosure import Aquatic
from staff import Zookeeper, Veterinarian


class TestStaff:

    @pytest.fixture
    def sample_zookeeper(self):
        jim = Zookeeper("Jim", 21, "Zookeeper", "Feeds Animals and Cleans the Enclosures")
        return jim

    @pytest.fixture
    def sample_veterinarian(self):
        bob = Veterinarian("Bob", 18, "Veterinarian", False)
        return bob

    @pytest.fixture
    def sample_animal(self):
        leo = Mammal("Leo", "Lion", 6, "Meat")
        return leo

    @pytest.fixture
    def sample_enclosure(self):
        aquatic = Aquatic("Aquatic", 1, "Aquatic", False)
        return aquatic

    @pytest.fixture
    def sample_staff_assign_enclosure(self, sample_zookeeper, sample_enclosure):
        return sample_zookeeper.staff_assign_enclosure(sample_enclosure)

    def test_add_enclosure(self, sample_staff_assign_enclosure):
        assert sample_staff_assign_enclosure is None

    def test_feed_animal(self, sample_zookeeper, sample_animal):
        assert sample_zookeeper.feed_animal(sample_animal) is None
        assert sample_zookeeper.feed_animal(sample_animal) == f"The animal {sample_animal.name} has been feed.\n"
        assert sample_animal.feed is True

    def test_clean_enclosure(self, sample_zookeeper, sample_enclosure):
        assert sample_enclosure.cleanliness is False
        assert sample_zookeeper.clean_enclosure(sample_enclosure) is None
        assert sample_enclosure.cleanliness is True

    def test_add_record(self, sample_animal, sample_zookeeper):
        assert sample_animal.animal_id == 1
        assert sample_animal.severity is None
        assert sample_animal.notes is None
        assert sample_zookeeper.notified is None
        assert sample_zookeeper.treatment_plan is None

    def test_health_check(self, sample_animal, sample_veterinarian):
        assert sample_veterinarian.health_check(sample_animal) == True

