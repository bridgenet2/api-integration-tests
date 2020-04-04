from unittest import TestCase

from .client import ApiIntegrationClient


class ApiIntegrationTestCase(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        headers = self.get_headers()
        self.client = ApiIntegrationClient(self.base_url, headers)

    def get(self, path=None, **kwargs):
        return self._make_request(path, 'get', **kwargs)

    def post(self, path=None, **kwargs):
        return self._make_request(path, 'post', **kwargs)

    def patch(self, path=None, **kwargs):
        return self._make_request(path, 'patch', **kwargs)

    def put(self, path=None, **kwargs):
        return self._make_request(path, 'put', **kwargs)

    def delete(self, path=None, **kwargs):
        return self._make_request(path, 'delete', **kwargs)

    def get_headers(self):
        return {}

    def _make_request(self, path, method, **kwargs):
        handler = getattr(self.client, method)
        if path is None:
            path = self.endpoint_path
        return handler(path, **kwargs)
