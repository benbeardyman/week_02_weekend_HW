class Bar:
    def __init__(self, till):
        self.till = till
        self.drinks_stock = {}


    def add_drink_to_drinks_stock(self, drink):
        if drink in self.drinks_stock:
            self.drinks_stock[drink] += 1
        else:
            self.drinks_stock[drink] = 1

    def stock_level(self, drink):
        if drink in self.drinks_stock:
            return self.drinks_stock[drink]
        else:
            return 0

    def stock_value(self):
        total = 0

        for drink in self.drinks_stock:
            total += (drink.price * self.drinks_stock[drink])

        return total

    def increase_money_in_till(self, amount):
        self.till += amount