from utils.Request import HTTPRequest

"""
    This class is used to get the coordinate of a city from the internet.
"""


class Coordinate:

    @staticmethod
    def get_coordinate_of_city_from_internet(city_name):
        """
        This method is used to get the coordinate of a city from the internet.
        :param city_name: city name
        :return: coordinate of the city
        """

        url = 'https://nominatim.openstreetmap.org/search.php'
        params = {
            'city': city_name,
            'format': 'jsonv2',
            'namedetails': 0,
            'addressdetails': 0,
        }
        http_request = HTTPRequest(url=url, params=params)
        response = None
        try:
            response = http_request.make_get_request(json=True)
        except Exception as e:
            print(e)
        if response is not None:
            if len(response) > 0 and 'lat' in response[0] and 'lon' in response[0]:
                return response[0]['lat'], response[0]['lon']
            else:
                print("No results found")
                return None
        print("No response")
        return None
