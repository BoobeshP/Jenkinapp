import unittest
from app import app

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "UP")

    def test_add(self):
        response = self.client.get("/add/2/3")
        self.assertEqual(response.json["result"], 5)

if __name__ == "__main__":
    unittest.main()
