import unittest
from datetime import datetime

import sys
sys.path.append("../..")

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serivced(self):
        tire_wear = [0.2, 0.5, 0.9, 0.9]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear = [0.4, 0.2, 0.4, 0.1]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serivced(self):
        tire_wear = [0.4, 0.9, 0.9, 0.8]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear = [0.2, 0.1, 0.4, 0.3]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
