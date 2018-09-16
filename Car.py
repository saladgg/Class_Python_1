class CarClass():
    def __init__(self, make, year, price):
        self.make = make
        self.year = year
        self.price = price

    def car_info(self):
        return "I am  %s year: %s market price: %s" % (self.make, self.year, self.price)
