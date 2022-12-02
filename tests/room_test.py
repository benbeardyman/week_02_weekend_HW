import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):



    def setUp(self):
        self.room1 = Room("The Red Room", 5)


    def test_room_has_name(self):
        self.assertEqual("The Red Room", self.room1.name)