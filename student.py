"""The student thread"""

import threading
import time
import random
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
        """Constructor"""
        super(Student, self).__init__()
        self.exam_1 = 0
        self.exam_2 = 0
        self.exam_3 = 0
        self.arrival_time = 1000
        Student.id_number += 1
        self.number = Student.id_number

    def run(self):
        """Implementing the thread run method"""
        print("The thread " + str(self.number) + " has started running...")
        sleep_time = random.randrange(5)
        print(str(self.number) + " is sleeping for "+ str(sleep_time) + " second(s)")
        time.sleep(sleep_time)
        print(str(self.number) + " is done!")
