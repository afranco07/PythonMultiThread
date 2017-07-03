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
        self.name = "Student-" + str(Student.id_number)
        Student.id_number += 1

    def print_grades(self):
        """Return the students grades"""
        return "exam 1 = " + str(self.exam_1) + "; exam 2 = " + str(self.exam_2) + \
               "; exam 3 = " + str(self.exam_3)
    
    def grade_exam(self):
        """
        Give a grade to exam, depending on which test 
        was taken
        """
        current_exam = Person.class_room.exam_number
        grade = random.randrange(100)

        if current_exam == 1:
            self.exam_1 = grade
        elif current_exam == 2:
            self.exam_2 = grade
        else:
            self.exam_3 = grade

    def run(self):
        """Implementing the thread run method"""
        threading.current_thread().setName(self.name)

        while True:
            if Person.class_room.exam_number > 3:
                break

            random_time = random.randrange(5)
            super().msg("will arrive in " + str(random_time) + " seconds...")
            time.sleep(random_time)
            super().msg("is here!")

            Student.mutex_semaphore.acquire()
            if Person.class_room.current_capacity < Person.class_room.max_capacity:
                super().msg("is waiting for class to open...")
                Person.class_room.current_capacity += 1
                Student.mutex_semaphore.release()

                Person.class_room.instructor_sem.acquire()
                super().msg("is in the class!")
                

