from unittest import TestCase


class Test(TestCase):
    def test_httprequest_no_url(self):
        from utils.Request import HTTPRequest
        with self.assertRaises(Exception):
            HTTPRequest().make_get_request()

    def test_httprequest_empty_url(self):
        from utils.Request import HTTPRequest
        with self.assertRaises(Exception):
            HTTPRequest(url="").make_get_request()

    def test_httprequest_no_json_url(self):
        from utils.Request import HTTPRequest
        with self.assertRaises(Exception):
            HTTPRequest(url="https://www.google.com").make_get_request()

    def test_httprequest_json_url(self):
        from utils.Request import HTTPRequest
        self.assertIsNotNone(HTTPRequest(url="https://www.google.com").make_get_request(json=False))
