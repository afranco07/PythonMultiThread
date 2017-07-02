"""The student thread"""

import threading
import time
from person import Person

class Student(Person, threading.Thread):
    """The student class"""

    id_number = 0
    mutex_semaphore = threading.Lock()
    num_students = 0
    remaining_students = Person.class_room.num_students
    group_number = 1
    leaving_student = 0

    def __init__(self):
        super(Student, self).__init__()
        self.exam_1 = 0
        self.exam_2 = 0
        self.exam_3 = 0
        self.arrival_time = 1000
        #self.number = id + 1

    def run(self):
        """Implementing the thread run method"""
        print("The thread has started running...")
        time.sleep(5)
        print("All done!")
