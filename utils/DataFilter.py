"""
Base Class for Data Filtering with interfaces for filtering data
"""


class DataFilter:
    def load_data(self, data):
        pass

    def update_data(self, data):
        pass

    def get_results_from_data(self, **kwargs):
        pass


"""
Class for filtering rain data
"""


class RainDataFilter(DataFilter):

    def __init__(self, distance_threshold, rain_threshold, data=None):
        """
        :param distance_threshold: distance threshold in degrees
        :param rain_threshold: rain threshold in mm
        :param data: data to be filtered
        """
        self.distance_threshold = distance_threshold
        self.rain_threshold = rain_threshold
        self.data = data

    # Method for loading data
    def load_data(self, data):
        self.data = data

    # Method for updating data
    def update_data(self, data):
        self.data = data

    def get_results_from_data(self, coordinate_latitude, coordinate_longitude):
        """
        :param coordinate_latitude: coordinate latitude
        :param coordinate_longitude: coordinate longitude
        :return: filtered data
        """
        dates = list()

        # Check if data is loaded
        if self.data is None:
            print("No data loaded")
            return dates

        if len(self.data) == 0:
            print("No data loaded")
            return dates

        # Check if coordinates are valid
        if coordinate_latitude is None or coordinate_longitude is None:
            print("Invalid coordinates")
            return dates

        try:
            float_coordinate_latitude = float(coordinate_latitude)
            float_coordinate_longitude = float(coordinate_longitude)
        except Exception as e:
            print(e)
            return dates

        # Check if thresholds are valid
        if self.distance_threshold is None \
                or self.rain_threshold is None \
                or (isinstance(self.distance_threshold, float) is False and isinstance(self.distance_threshold,
                                                                                       int) is False) \
                or (isinstance(self.rain_threshold, float) is False and isinstance(self.rain_threshold, int) is False):
            print("Invalid thresholds")
            return dates

        for row in self.data:
            t, lat, lon, rain = row
            # Check if row is valid
            if len(t) < 10 or len(lat) == 0 or len(lon) == 0 or len(rain) == 0:
                continue
            t = t[:10]

            # Check if rain is valid
            if rain != "NaN":
                try:
                    float_lat = float(lat)
                    float_lon = float(lon)
                    float_rain = float(rain)
                except Exception as e:
                    print(e)
                    continue

                lat_diff = abs(float_lat - float_coordinate_latitude)
                lon_diff = abs(float_lon - float_coordinate_longitude)
                # Check if rain, lat and lon are within threshold
                if float_rain >= self.rain_threshold \
                        and lat_diff < self.distance_threshold \
                        and lon_diff < self.distance_threshold:
                    dates.append((t, rain))

        return dates
