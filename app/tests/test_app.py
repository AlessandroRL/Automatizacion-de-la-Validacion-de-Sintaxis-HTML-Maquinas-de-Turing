import unittest
from app import app
from app.utils import validate_html, validate_url

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home_page(self):
        """Prueba que la página principal cargue correctamente."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Validador HTML', response.data)

    def test_validate_html(self):
        """Prueba la función de validación de código HTML."""
        html = "<!DOCTYPE html><html><head><title>Test</title></head><body></body></html>"
        result = validate_html(html)
        self.assertIn("messages", result)

    def test_validate_url(self):
        """Prueba la función de validación de URL."""
        test_url = "https://www.w3.org/"
        result = validate_url(test_url)
        self.assertIn("messages", result)

    def test_invalid_route(self):
        """Prueba el manejo de rutas no válidas."""
        response = self.client.get('/invalid')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
