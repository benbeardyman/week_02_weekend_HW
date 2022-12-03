import unittest
from classes.song import Song

class TestSong(unittest.TestCase):



    def setUp(self):
        self.song1 = Song("Mr Your On Fire Mr", "Liars", "Noise Rock", 2.5)

    
    def test_song_has_name(self):
        self.assertEqual("Mr Your On Fire Mr", self.song1.song_title)