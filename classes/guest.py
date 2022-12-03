class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def remove_money_from_wallet(self, amount):
        self.wallet -= amount