import unittest
import MCD

class TestCalculator(unittest.TestCase):
    def test_mcd_1(self):
        self.assertEqual(MCD.mcd(-1,0), -1)
        self.assertEqual(MCD.mcd(1,-1), -1)
        self.assertEqual(MCD.mcd(1,1), 1)
        self.assertEqual(MCD.mcd(2,1), 1)
        self.assertEqual(MCD.mcd(2,2), 2)
        self.assertEqual(MCD.mcd(6,3), 3)
        self.assertEqual(MCD.mcd(3,6), 3)
        
