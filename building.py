'''
Realises classes Building and House.
'''

class Building():
    '''
    The base class for House and AcademicBuilding.
    '''

    def __init__(self, address: str):
        '''
        :param address: The address of the building.
        '''
        self.address = address


class House(Building):
    '''
    Represents blocks of flats.
    '''

    def __init__(self, address: str, flats: list):
        '''
        :param address: The string with the address; inherited from Building.
        :param flats: The list of flats in the building.
        '''
        super().__init__(address)
        self.flats = flats
