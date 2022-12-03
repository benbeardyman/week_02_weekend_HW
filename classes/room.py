class Room:
    def __init__(self, name, capacity, till, entry_fee):
        self.name = name
        self.capacity = capacity
        self.till = till
        self.entry_fee = entry_fee
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

    def increase_money_in_till(self, amount):
        self.till += amount

    def admit_guest_to_room(self, guest):
        if len(self.guest_list) < 5:
            self.add_guest_to_room(guest)
            guest.remove_money_from_wallet(self.entry_fee)
            self.increase_money_in_till(self.entry_fee)
        else:
            return "Sorry, no entry, the room is full"
