"""The instructor thread"""

import threading
import time
import random
from person import Person

class Instructor(Person, threading.Thread):
    """The instructor class definition"""
    
    def __init__(self):
        super(Instructor, self).__init__()
        self.name = "Instructor"

    def run(self):
        threading.current_thread().setName(self.name)

        while True:
            if Person.class_room.exam_number > 3:
                break

            random_time = random.randrange(5)
            super().msg("will arrive in " + str(random_time) + " seconds...")
            time.sleep(random_time)
            super().msg("is here! Students may enter the class!")
            super().msg("waiting for the seats to fill up...")
            for _ in range(Person.class_room.max_capacity):
                Person.class_room.instructor_sem.release()

            Person.class_room.seats_semaphore.acquire(Person.class_room.max_capacity)
            super().msg("Class closed! Seats are filled!")
            super().msg("Exam in progress...")
            Person.class_room.count = 0

            for _ in range(Person.class_room.max_capacity):
                Person.class_room.start_exam.release()
            
            time.sleep(10)
            super().msg("Exam over! Collecting exams now...")
            Person.WAIT_FLAG.set()
            Person.class_room.exam_number += 1
            time.sleep(2)
            Person.WAIT_FLAG.clear()

            Person.class_room.end_exam.acquire(Person.class_room.max_capacity)

            for _ in range(Person.class_room.missed_students):
                Person.class_room.missed_exam.release()
            
            Person.class_room.missed_students = 0
            Person.class_room.seats.clear()
            Person.class_room.current_capacity = 0
            super().take_break()

        Person.class_room.i_am_done.acquire(Person.class_room.max_capacity)
        for _ in range(Person.class_room.num_students):
            Person.class_room.wait_for_finish.release()
        Person.class_room.i_am_done.acquire(Person.class_room.num_students)
        for _ in range(Person.class_room.num_students):
            Person.class_room.wait_for_finish.release()

        Person.class_room.go_home_prof.acquire(Person.class_room.num_students)
        time.sleep(1)
        super().msg("All of the students are gone. I can go home now :D")