import unittest
from app.turing import validate_url

class TestTuringMachine(unittest.TestCase):
    def test_valid_url(self):
        self.assertEqual(validate_url("https://example.com"), "https://example.com")

    def test_invalid_url(self):
        self.assertNotEqual(validate_url("invalid_url"), "invalid_url")

if __name__ == '__main__':
    unittest.main()
