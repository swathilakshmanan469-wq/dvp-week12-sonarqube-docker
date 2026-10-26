
import unittest
from app import greet


class TestGreeting(unittest.TestCase):
    def test_greet_name(self):
        self.assertEqual(greet("Swathi"), "Hello, Swathi!")

    def test_greet_empty(self):
        self.assertEqual(greet(""), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
