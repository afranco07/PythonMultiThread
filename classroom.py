"""The classroom variable that is shared by the instructor and student threads"""

import threading

class ClassRoom(object):
    """The classroom class"""

    def __init__(self, max, num_students, group):
        self.current_capacity = 0
        self.max_capacity = max
        self.exam_number = 1
        self.priority = 10
        self.missed_students = 0
        self.count = 0
        self.num_students = num_students
        self.group = group
        self.seats = []