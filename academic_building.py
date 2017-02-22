from classroom import Classroom

class AcademicBuilding():

    def __init__(self, address: str, classrooms: list):
        self.address = address
        self.classrooms = classrooms

    def __str__(self):
        return '\n'.join([self.address] + [str(classroom) for classroom in self.classrooms])

    def total_equipment(self):
        equipment = {}
        for classroom in self.classrooms:
            for equip in classroom.equipment:
                if equip not in equipment:
                    equipment.update({equip: 1})
                else:
                    equipment[equip] += 1
        return tuple(((equip, equipment[equip]) for equip in equipment))
