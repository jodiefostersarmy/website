import unittest
from main import create_app

class TestPosts(unittest.TestCase):
    @classmethod
    def setUp(cls):
        print("setup ran")

    @classmethod
    def tearDown(cls):
        print("teardown ran")

    def test_post_index(self):
        app = create_app()
        client = app.test_client()
        response = client.get("/posts/")

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

