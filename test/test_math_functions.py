import unittest
from unittest import mock

from src import math_functions as my_math


class TestMath(unittest.TestCase):
    def setUp(self):
        pass

    def test_complex_math(self):
        """Is the complex math still working accordingly?"""
        output = my_math.complex_math(1, 2)
        expected_output = 3

        self.assertEqual(output, expected_output)
