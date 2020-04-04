from unittest import defaultTestLoader, TestCase, TextTestRunner
from unittest.mock import patch

from pronym_api_integration_tests import ApiIntegrationTestCase, ApiResponse


class FakeResponse:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content


@patch('pronym_api_integration_tests.client.requests', autospec=True)
class ExampleTestCase(TestCase):

    def setUp(self):
        # Construct a sample test case, and we'll fake the requests to verify
        # it passes / fails as expected.
        class UnauthenticatedApiIntegrationTestCase(ApiIntegrationTestCase):
            base_url = "http://api.pronym.com/v1/"
            endpoint_path = "account/"

            is_authenticated = False

            def get_headers(self):
                return {'Authorization': 'Token 12345'}

            def test_create_account(self):
                response = self.post(data={
                    'name': 'Gregg Kreezles',
                    'age': 18
                })

                self.assertEqual(response.status_code, 200)

                self.assertIn('id', response.json)

        self.test_case = UnauthenticatedApiIntegrationTestCase

    def _execute_tests(self):
        suite = defaultTestLoader.loadTestsFromTestCase(self.test_case)
        runner = TextTestRunner()
        return runner.run(suite)

    def test(self, _requests):
        _requests.post.return_value = ApiResponse(
            200,
            """{"id": 123, "name": "Gregg Kreezles", "age": 18}"""
        )

        self.assertTrue(self._execute_tests().wasSuccessful())

        _requests.post.assert_called_once_with(
            "http://api.pronym.com/v1/account/",
            data={
                "name": "Gregg Kreezles",
                "age": 18
            },
            headers={'Authorization': 'Token 12345'}
        )
