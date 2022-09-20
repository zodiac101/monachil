from unittest import TestCase

from utils.Coordinate import Coordinate
from utils.DataFilter import RainDataFilter
from utils.File import CSVFile


class Test(TestCase):
    def test_main(self):
        input_file = CSVFile('files/test_file.csv')
        rain_data = input_file.read()
        c_lat, c_lon = Coordinate.get_coordinate_of_city_from_internet('San Jose')
        dist_thresh = 0.05
        rain_thresh = 8.0

        rain_data_filter = RainDataFilter(distance_threshold=dist_thresh, rain_threshold=rain_thresh, data=rain_data)
        dates = rain_data_filter.get_results_from_data(coordinate_latitude=c_lat, coordinate_longitude=c_lon)

        # dates=sorted(list(set(dates)))
        for item in dates:
            print(item)
        print("number of rainy 5-days: " + str(len(dates)))
        self.assertEqual(len(dates), 8)
