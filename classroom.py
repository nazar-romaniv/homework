'''
Module implementing Classroom class.
'''

class Classroom():
    '''
    Class to represent classrooms in a classroom management program.
    '''

    def __init__(self, number: str, capacity: int, equipment: list):
        '''
        (str, int, list(str))
        :param number: Number of the classroom.
        :param capacity: The maximum number of students.
        :param equipment: THe equipment available in the classroom.
        '''
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __gt__(self, other):
        '''
        Describes the comparison of two classrooms.
        If self has a higher capacity than other, returns True.
        '''
        if self.capacity > other.capacity:
            return True
        else:
            return False

    def __lt__(self, other):
        '''
        Returns True if self has a lower capacity than other.
        '''
        if self.capacity < other.capacity:
            return True
        else:
            return False

    def __le__(self, other):
        '''
        Returns True if the capacity of self is lower than or the same as other.
        '''
        if self.capacity <= other.capacity:
            return True
        else:
            return False

    def __ge__(self, other):
        '''
        Returns True if the capacity of self is higher than or the same as other.
        '''
        if self.capacity >= other.capacity:
            return True
        else:
            return False

    def __eq__(self, other):
        '''
        Returns True if the capacity of self is equal to that of other.
        '''
        if self.capacity == other.capacity:
            return True
        else:
            return False

    def is_larger(self, other):
        '''
        Returns True if self is bigger.
        '''
        return self > other

    def equipment_difference(self, other) -> list:
        '''
        Returns the list of the pieces of equipment available in self but not other.
        '''
        equipment = list()
        for equip in self.equipment:
            if equip not in other.equipment:
                equipment.append(equip)
        return equipment

    def __str__(self):
        '''
        Returns the string describing the classroom.
        '''
        return 'Classroom {0} has a capacity of {1} and has the following equipment: {2}.'.format(
            self.number,
            self.capacity,
            ', '.join(self.equipment)
            )

    def __repr__(self):
        '''
        Returns the string representation of the object.
        '''
        return 'Classroom({0}, {1}, {2})'.format(repr(self.number), self.capacity, self.equipment)
