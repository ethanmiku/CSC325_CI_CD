
from django.test import SimpleTestCase


class StatusEndpointTests(SimpleTestCase):

    def test_status_returns_200(self):
        response = self.client.get("/api/status/")
        self.assertEqual(response.status_code, 200)

    def test_status_response(self):
        response = self.client.get("/api/status/")

        self.assertEqual(response.json()["status"], "ok")
        self.assertEqual(
            response.json()["service"],
            "RoomBook API"
        )
        self.assertEqual(response.json()["version"], "1.0")
