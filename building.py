class Building():

    def __init__(self, address):
        self.address = address


class House(Building):

    def __init__(self, address, flats):
        super().__init__(address)
        self.flats = flats
