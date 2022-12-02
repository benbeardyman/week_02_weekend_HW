class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guest_list = []
        self.song_list = []


    def number_of_people_in_room(self):
        return len(self.guest_list)

    def add_guest_to_room(self, guest):
        self.guest_list.append(guest)

    def remove_guest_from_room(self, guest):
        self.guest_list.remove(guest)

    def number_of_songs_in_song_list(self):
        return len(self.song_list)

    def add_song_to_song_list(self, song):
        self.song_list.append(song)