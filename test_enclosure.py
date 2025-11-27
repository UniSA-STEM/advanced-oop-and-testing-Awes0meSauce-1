import pytest

from enclosure import Enclosure, Aquatic
from main import leo
from main import dip


class TestEnclosure:

    @pytest.fixture
    def sample_enclosure(self):
        aquatic = Aquatic("Aquatic", 1, "Aquatic", False)
        return aquatic

    @pytest.fixture
    def sample_enclosure_none(self, sample_enclosure):
        return sample_enclosure.check_type(leo)

    @pytest.fixture
    def sample_enclosure_false(self, sample_enclosure):
        sample_enclosure.animal_assign_enclosure(leo)
        return sample_enclosure.check_type(leo)

    @pytest.fixture
    def sample_enclosure_true(self, sample_enclosure):
        return sample_enclosure.check_type(dip)

    @pytest.fixture
    def sample_enclosure_size_false(self, sample_enclosure):
        return sample_enclosure.check_size(leo)

    @pytest.fixture
    def sample_enclosure_size_true(self, sample_enclosure):
        sample_enclosure.animal_assign_enclosure(leo)
        return sample_enclosure.check_size(leo)

    def test_enclosure(self, sample_enclosure):
        assert sample_enclosure.name == "Aquatic"
        assert sample_enclosure.size == 1
        assert sample_enclosure.environmental_type == "Aquatic"
        assert sample_enclosure.cleanliness == False

    def test_enclosure_type(self, sample_enclosure_none, sample_enclosure_false, sample_enclosure_true):
        assert sample_enclosure_none is None
        assert sample_enclosure_false is False
        assert sample_enclosure_true is True

    def test_enclosure_size(self, sample_enclosure_size_false, sample_enclosure_size_true):
        assert sample_enclosure_size_false == False
        assert sample_enclosure_size_true == True

    def test_generate_report(self, sample_enclosure):
        assert sample_enclosure.id == 7
        assert sample_enclosure.name == "Aquatic"
        assert sample_enclosure.size == 1
        assert sample_enclosure.environmental_type == "Aquatic"
        assert sample_enclosure.cleanliness == False