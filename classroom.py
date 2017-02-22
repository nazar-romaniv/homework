class Classroom():

    def __init__(self, number, capacity, equipment):
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __gt__(self, other):
        if self.capacity > other.capacity:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.capacity < other.capacity:
            return True
        else:
            return False

    def __le__(self, other):
        if self.capacity <= other.capacity:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.capacity >= other.capacity:
            return True
        else:
            return False

    def is_larger(self, other):
        return self > other

    def equipment_difference(self, other):
        equipment = list()
        for equip in self.equipment:
            if equip not in other.equipment:
                equipment.append(equip)
        return equipment

    def __str__(self):
        return 'Classroom {0} has a capacity of {1} and has the following equipment: {2}'.format(
                                                                                            self.number,
                                                                                            self.capacity,
                                                                                            ','.join(self.equipment))

    def __repr__(self):
        return 'Classroom({0}, {1}, {2})'.format(repr(self.number), self.capacity, self.equipment)
