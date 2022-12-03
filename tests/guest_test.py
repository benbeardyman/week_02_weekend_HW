import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):



    def setUp(self):
        self.guest1 = Guest("Tim", 60)


    def test_guest_has_name(self):
        self.assertEqual("Tim", self.guest1.name)
    
    def test_guest_has_money(self):
        self.assertEqual(60, self.guest1.wallet)

    def test_remove_money_from_wallet(self):
        self.guest1.remove_money_from_wallet(3)
        self.assertEqual(57, self.guest1.wallet)