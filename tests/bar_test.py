import unittest
from classes.bar import Bar
from classes.drink import Drink
from classes.guest import Guest

class TestBar(unittest.TestCase):


    def setUp(self):
        self.bar = Bar(200)
        self.drink1 = Drink("Beer", 5)
        self.drink2 = Drink("Wine", 6)
        self.drink3 = Drink("Mojito", 9)
        self.guest = Guest("Tim", 7, "Mr Your On Fire Mr")

    def test_bar_has_till(self):
        self.assertEqual(200, self.bar.till)

    def test_bar_stock_starts_at_0(self):
        self.assertEqual(0, self.bar.stock_level(self.drink1))

    def test_bar_value_starts_at_0(self):
        self.assertEqual(0, self.bar.stock_value())

    def test_add_drink_to_drinks_stock(self):
        self.bar.add_drink_to_drinks_stock(self.drink1)
        self.assertEqual(5, self.bar.stock_value())

    def test_add_drink_to_drinks_stock_value(self):
        self.bar.add_drink_to_drinks_stock(self.drink1)
        self.assertEqual(5, self.bar.stock_value())

    def test_increase_money_in_till(self):
        self.bar.increase_money_in_till(5)
        self.assertEqual(205, self.bar.till)

    def test_guest_can_buy_drink_money_paid(self):
        self.add_drink_to_drinks_stock(drink1)
        self.guest_can_buy_drink(self.guest, self.drink1)
        self.assertEqual(2, self.guest.wallet)
        self.assertEqual(205, self.bar.till)

    def test_guest_can_buy_drink_stock_reduces(self):
        self.add_drink_to_drinks_stock(drink1)
        self.add_drink_to_drinks_stock(drink1)
        self.guest_can_buy_drink(self.guest, self.drink1)
        self.assertEqual(1, self.bar.stock_level(drink1))

