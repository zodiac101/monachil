from unittest import TestCase


class Test(TestCase):

    def test_coordinate_get_coordinate_of_city_from_internet_no_city(self):
        from utils.Coordinate import Coordinate
        self.assertIsNone(Coordinate.get_coordinate_of_city_from_internet(None))

    def test_coordinate_get_coordinate_of_city_from_internet_blank_city(self):
        from utils.Coordinate import Coordinate
        self.assertIsNone(Coordinate.get_coordinate_of_city_from_internet(""))

    def test_coordinate_get_coordinate_of_city_from_internet_invalid_city(self):
        from utils.Coordinate import Coordinate
        self.assertIsNone(Coordinate.get_coordinate_of_city_from_internet("Sam Jose"))

    def test_coordinate_get_coordinate_of_city_from_internet(self):
        from utils.Coordinate import Coordinate
        res = Coordinate.get_coordinate_of_city_from_internet("San Jose")
        self.assertIsNotNone(res)
        self.assertIsNotNone(res[0])
        self.assertIsNotNone(res[1])
        self.assertEqual(len(res), 2)
