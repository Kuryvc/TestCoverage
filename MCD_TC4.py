import unittest
import MCD

class TestCalculator(unittest.TestCase):
    def test_mcd_1(self):
        self.assertEqual(MCD.mcd(2,1), 1)
