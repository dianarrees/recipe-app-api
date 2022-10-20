"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        result = calc.add(5, 6)

        self.assertEqual(result, 11)

    def test_subtract_numbers(self):
        """Test adding numbers together"""
        result = calc.subtract(10, 15)

        self.assertEqual(result, 5)
