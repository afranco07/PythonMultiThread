"""The classroom variable that is shared by the instructor and student threads"""

import threading

class ClassRoom(object):
    """The classroom class"""

    def __init__(self, max_number, num_students, group):
        self.current_capacity = 0
        self.max_capacity = max_number
        self.exam_number = 1
        self.priority = 10
        self.missed_students = 0
        self.count = 0
        self.num_students = num_students
        self.group = group
        self.seats = []

        self.instructor_sem = threading.Semaphore(0)
        self.seats_semaphore = threading.Semaphore(0)
        self.start_exam = threading.Semaphore(0)
        self.end_exam = threading.Semaphore(0)
        self.missed_exam = threading.Semaphore(0)
        self.wait_for_finish = threading.Semaphore(0)
        self.i_am_done = threading.Semaphore(0)
        self.go_home_prof = threading.Semaphore(0)
