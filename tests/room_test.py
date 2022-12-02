import unittest
from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):



    def setUp(self):
        self.room1 = Room("The Red Room", 5)
        self.guest1 = Guest("Tim")
        self.guest2 = Guest("Hayley")
        self.guest3 = Guest("Luke")
        self.guest4 = Guest("Phil")


    def test_room_has_name(self):
        self.assertEqual("The Red Room", self.room1.name)

    def test_room_starts_empty(self):
        self.assertEqual(0, self.room1.number_of_people_in_room())

    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.assertEqual(1, self.room1.number_of_people_in_room())

    def test_remove_guest_from_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.add_guest_to_room(self.guest3)
        self.room1.remove_guest_from_room(self.guest2)
        self.assertEqual(2, self.room1.number_of_people_in_room())