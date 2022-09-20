from unittest import TestCase


class TestRainDataFilter(TestCase):

    def setUp(self):
        self.sample_data_correct = [
            ['2021-11-26T00:00:00Z', '38.024994', '-117.825005', '1.37942004'],
            ['2021-11-26T00:00:00Z', '38.024994', '-117.77501', '1.26905638'],
            ['2021-11-26T00:00:00Z', '38.024994', '-117.725006', '0.20762266'],
            ['2021-11-26T00:00:00Z', '38.024994', '-117.675', '0.24495272'],
            ['2021-11-26T00:00:00Z', '139.024994', '-218.725006', '1.20762266'],
            ['2021-11-26T00:00:00Z', '139.024994', '-218.675', '1.24495272']
        ]

        self.sample_data_incorrect = [
            ['2021-11-', '38.024994', '-117.825005', '0.37942004'],
            ['2021-11-26T00:00:00Z', 'abd', '-117.77501', '0.26905638'],
            ['2021-11-26T00:00:00Z', '38.024994', 'anc', '0.20762266'],
            ['2021-11-26T00:00:00Z', '38.024994', '-117.675', 'abcd'],
            ['', '38.024994', '-117.825005', '0.37942004'],
            ['2021-11-26T00:00:00Z', '', '-117.77501', '0.26905638'],
            ['2021-11-26T00:00:00Z', '38.024994', '', '0.20762266'],
            ['2021-11-26T00:00:00Z', '38.024994', '-117.675', ''],
            ['2021-11-26T00:00:00Z', '38.024994', '-117.675', '0.24495272']
        ]

    def test_get_results_from_data_no_data(self):
        from utils.DataFilter import RainDataFilter
        self.assertEqual(RainDataFilter(distance_threshold=0, rain_threshold=0).get_results_from_data(
            coordinate_latitude=0, coordinate_longitude=0), list())

    def test_get_results_from_data_no_data_loaded(self):
        from utils.DataFilter import RainDataFilter
        self.assertEqual(RainDataFilter(distance_threshold=0, rain_threshold=0, data=list()).get_results_from_data(
            coordinate_latitude=0, coordinate_longitude=0), list())

    def test_get_results_from_data_invalid_thresholds(self):
        from utils.DataFilter import RainDataFilter
        self.assertEqual(RainDataFilter(distance_threshold=None, rain_threshold=None,
                                        data=self.sample_data_correct).get_results_from_data(
            coordinate_latitude=0, coordinate_longitude=0), list())

    def test_get_results_from_data_invalid_thresholds_2(self):
        from utils.DataFilter import RainDataFilter
        self.assertEqual(RainDataFilter(distance_threshold=0, rain_threshold=None,
                                        data=self.sample_data_correct).get_results_from_data(
            coordinate_latitude=0, coordinate_longitude=0), list())

    def test_get_results_from_data_invalid_thresholds_3(self):
        from utils.DataFilter import RainDataFilter
        self.assertEqual(RainDataFilter(distance_threshold=None, rain_threshold=0,
                                        data=self.sample_data_correct).get_results_from_data(
            coordinate_latitude=0, coordinate_longitude=0), list())

    def test_get_results_from_data_invalid_thresholds_4(self):
        from utils.DataFilter import RainDataFilter
        self.assertEqual(RainDataFilter(distance_threshold="0", rain_threshold="0",
                                        data=self.sample_data_correct).get_results_from_data(
            coordinate_latitude=0, coordinate_longitude=0), list())

    def test_get_results_from_data_invalid_thresholds_5(self):
        from utils.DataFilter import RainDataFilter
        self.assertEqual(RainDataFilter(distance_threshold=0, rain_threshold="0",
                                        data=self.sample_data_correct).get_results_from_data(
            coordinate_latitude=0, coordinate_longitude=0), list())

    def test_get_results_from_data_invalid_thresholds_6(self):
        from utils.DataFilter import RainDataFilter
        self.assertEqual(RainDataFilter(distance_threshold="0", rain_threshold=0,
                                        data=self.sample_data_correct).get_results_from_data(
            coordinate_latitude=0, coordinate_longitude=0), list())

    def test_get_results_from_data_invalid_coordinates(self):
        from utils.DataFilter import RainDataFilter
        self.assertEqual(
            RainDataFilter(distance_threshold=0, rain_threshold=0, data=self.sample_data_correct).get_results_from_data(
                coordinate_latitude=None, coordinate_longitude=None), list())

    def test_get_results_from_data_incorrect_data(self):
        from utils.DataFilter import RainDataFilter
        self.assertEqual(
            len(RainDataFilter(distance_threshold=100, rain_threshold=0,
                               data=self.sample_data_incorrect).get_results_from_data(
                coordinate_latitude='-38', coordinate_longitude='-117')), 1)

    def test_get_results_from_data_correct_data(self):
        from utils.DataFilter import RainDataFilter
        self.assertEqual(
            len(RainDataFilter(distance_threshold=100, rain_threshold=1,
                               data=self.sample_data_correct).get_results_from_data(
                coordinate_latitude='-38', coordinate_longitude='-117')), 2)
