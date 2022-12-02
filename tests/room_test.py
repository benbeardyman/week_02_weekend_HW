import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):



    def setUp(self):
        self.room1 = Room("The Red Room", 5)
        self.guest1 = Guest("Tim")
        self.guest2 = Guest("Hayley")
        self.guest3 = Guest("Luke")
        self.guest4 = Guest("Phil")
        self.song1 = Song("Dance", "ESG", "Funk", 4.5)
        self.song2 = Song("Gyae Su", "Pat Thomas", "Highlife", 4)
        self.song3 = Song("Little Fluffy Clouds", "The Orb", "Electronic", 4.5)
        self.song4 = Song("Love and Death", "Ebo Taylor", "Highlife", 7 )



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

    def test_song_list_starts_empty(self):
        self.assertEqual(0, self.room1.number_of_songs_in_song_list())

    def test_add_song_to_song_list(self):
        self.room1.add_song_to_song_list(self.song1)
        self.assertEqual(1, self.room1.number_of_songs_in_song_list())