import unittest
from cal import sub

class TestMyMath(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(sub(2, 3), -3)

    def test_add_negative_numbers(self):
        self.assertEqual(sub(-2, -3), 1)

    def test_add_mixed_numbers(self):
        self.assertEqual(sub(2, -3), 5)

if __name__ == '_main__':
    unittest.main()
