import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):



    def setUp(self):
        self.room1 = Room("The Red Room", 5, 500, 3)
        self.guest1 = Guest("Tim", 60, "Mr Your On Fire Mr")
        self.guest2 = Guest("Hayley", 50, "Deceptacon")
        self.guest3 = Guest("Luke", 70, "Hey Moon!")
        self.guest4 = Guest("Phil", 85, "Deceptacon")
        self.guest5 = Guest("Mark", 40, "Gyae Su")
        self.guest6 = Guest("Sam", 55, "Hey Moon!")
        self.song1 = Song("Hey Moon!", "Molly Nilsson", "Synth Pop", 5.5)
        self.song2 = Song("Gyae Su", "Pat Thomas", "Highlife", 4.0)
        self.song3 = Song("When I Grow Up", "Fever Ray", "Electro Pop", 4.5)
        self.song4 = Song("Deceptacon", "Le Tigre", "Electro Pop", 3.0)
        self.song5 = Song("Mr Your On Fire Mr", "Liars", "Noise Rock", 2.5)



    def test_room_has_name(self):
        self.assertEqual("The Red Room", self.room1.name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room1.capacity)

    def test_room_starts_empty(self):
        self.assertEqual(0, self.room1.number_of_people_in_room())

    def test_room_has_till(self):
        self.assertEqual(500, self.room1.till)

    def test_room_has_entry_fee(self):
        self.assertEqual(3, self.room1.entry_fee)

    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.assertEqual(1, self.room1.number_of_people_in_room())

    def test_remove_guest_from_room(self):
        self.room1.guest_list = [self.guest1, self.guest2, self.guest3]
        self.room1.remove_guest_from_room(self.guest2)
        self.assertEqual(2, self.room1.number_of_people_in_room())

    def test_song_list_starts_empty(self):
        self.assertEqual(0, self.room1.number_of_songs_in_song_list())

    def test_add_song_to_song_list(self):
        self.room1.add_song_to_song_list(self.song1)
        self.assertEqual(1, self.room1.number_of_songs_in_song_list())

    def test_increase_money_in_till(self):
        self.room1.increase_money_in_till(3)
        self.assertEqual(503, self.room1.till)

    def test_can_admit_guest_to_room(self):
        self.room1.admit_guest_to_room(self.guest1)
        self.assertEqual(1, self.room1.number_of_people_in_room())
        self.assertEqual(503, self.room1.till)
        self.assertEqual(57, self.guest1.wallet)

    def test_room_full_cant_admit_guest_to_room(self):
        self.room1.guest_list = [self.guest1, self.guest2, self.guest3, self.guest4, self.guest5]
        self.assertEqual("Sorry, no entry, the room is full", self.room1.admit_guest_to_room(self.guest6))

    def test_guest_cheers_if_favourite_song_on_song_list(self):
        self.room1.song_list = [self.song1, self.song3, self.song4]
        self.assertEqual("Cheer", self.room1.guest_cheers_if_favourite_song_on_song_list(self.guest2))
