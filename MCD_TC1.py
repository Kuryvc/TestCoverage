import unittest
import MCD

class TestCalculator(unittest.TestCase):
    def test_mcd_1(self):
        self.assertEqual(MCD.mcd(-1,0), -1)
