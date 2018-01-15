class School(object):
    def __init__(self, name):
        self.name = name
        self.classes = {}

    def add(self, student, grade):
        self.classes[grade] = self.classes.get(grade, []) + [student]

    def grade(self, number):
        return self.classes.get(number, [])

    def sort(self):
        return sorted([(grade, tuple(sorted(students))) for grade, students in self.classes.items()])
