import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):



    def setUp(self):
        self.guest1 = Guest("Tim")


    def test_guest_has_name(self):
        self.assertEqual("Tim", self.guest1.name)