from json import loads
from urllib.parse import urljoin

import requests


class ApiResponse:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content

    @property
    def json(self):
        if not hasattr(self, '_json'):
            self._json = loads(self.content)
        return self._json


class ApiIntegrationClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path, **kwargs):
        # Rename data to params for get request.
        if 'data' in kwargs:
            kwargs['params'] = kwargs.pop('data')
        return self._execute_request(path, 'get', **kwargs)

    def post(self, path, *args, **kwargs):
        return self._execute_request(path, 'post', **kwargs)

    def put(self, path, *args, **kwargs):
        return self._execute_request(path, 'put', **kwargs)

    def patch(self, path, *args, **kwargs):
        return self._execute_request(path, 'patch', **kwargs)

    def delete(self, path, *args, **kwargs):
        return self._execute_request(path, 'delete', **kwargs)

    def _execute_request(self, path, method, **kwargs):
        url = self._get_url(path)
        if method in ('get', 'post', 'put', 'patch', 'delete'):
            handler = getattr(requests, method)
        response = handler(url, **kwargs)
        return self._make_response(response)

    def _get_url(self, path):
        return urljoin(self.base_url, path)

    def _make_response(self, requests_response):
        return ApiResponse(
            requests_response.status_code,
            requests_response.content
        )
