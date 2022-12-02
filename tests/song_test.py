import unittest
from classes.song import Song

class TestSong(unittest.TestCase):


   
    def setUp(self):
        self.song1 = Song("Dance", "ESG", "Funk", 4.5)

    
    def test_song_has_name(self):
        self.assertEqual("Dance", self.song1.song_title)