import requests

"""
    Basic request class
"""
class Request:
    def make_get_request(self):
        pass

    def make_post_request(self):
        pass

    def make_put_request(self):
        pass

    def make_delete_request(self):
        pass

"""
    HTTP request class
"""
class HTTPRequest(Request):
    def __init__(self, url=None, params=None, payload=None, headers=None):
        """
        Constructor
        :param url: url
        :param params: params
        :param payload: payload
        :param headers: headers
        """
        self.url = url
        self.params = params
        self.payload = payload
        self.headers = headers

    def make_get_request(self, json=True):
        """
        Make a get request
        :param json: if the response should be json
        :return: response
        """
        if self.url is None:
            raise Exception("URL is not defined")
        response = requests.get(
            params=self.params,
            url=self.url,
            data=self.payload,
            headers=self.headers
        )
        if response.status_code == 200:
            if json:
                return response.json()
            else:
                return response.text
        else:
            raise Exception("Request failed with code: {}".format(response.status_code))
