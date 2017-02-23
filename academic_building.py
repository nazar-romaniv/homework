'''
Realises the class AcademicBuilding to contain objects of the class Classroom.
'''

from building import Building
from classroom import Classroom

class AcademicBuilding(Building):
    '''
    Class to represent academic buildings and contain instances of Classroom.
    '''

    def __init__(self, address: str, classrooms: list):
        '''
        :param address: Inherited from Building.
        :param classrooms: The list of classrooms in the building.
        '''
        super(AcademicBuilding, self).__init__(address)
        self.classrooms = classrooms

    def __str__(self):
        return '\n'.join([self.address] + [str(classroom) for classroom in self.classrooms])

    def total_equipment(self) -> tuple:
        '''
        Returns a tuple with the total number of pieces of equipment of each kind in the builing.
        '''
        equipment = {}
        for classroom in self.classrooms:
            for equip in classroom.equipment:
                if equip not in equipment:
                    equipment.update({equip: 1})
                else:
                    equipment[equip] += 1
        return tuple(((equip, equipment[equip]) for equip in equipment))
