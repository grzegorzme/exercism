class Garden(object):
    plant_map = {
        'C': 'Clover',
        'G': 'Grass',
        'R': 'Radishes',
        'V': 'Violets'
    }

    def __init__(self, diagram, students=None):
        self.students = sorted(['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
                                'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry'])
        if students:
            self.students = sorted(students)

        self.plant_dict = {}
        for row in diagram.split('\n'):
            for i in range(len(row)):
                student = self.students[i // 2]
                self.plant_dict[student] = self.plant_dict.get(student, '') + row[i]

    def plants(self, student):
        return [self.plant_map.get(plant) for plant in self.plant_dict.get(student)]
