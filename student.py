"""The student thread"""

import threading
import time
import random
from person import Person

class Student(Person, threading.Thread):
    """The student class"""

    id_number = 0
    mutex_semaphore = threading.Lock()
    group_semaphore = threading.Semaphore(0)
    num_students = 0
    remaining_students = Person.class_room.num_students
    group_number = 1
    temp_group_num = 1
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

                Person.class_room.seats.append(threading.current_thread())

                Student.mutex_semaphore.acquire()
                Person.class_room.count += 1
                if Person.class_room.count == Person.class_room.max_capacity:
                    super().msg("Professor close the door! I got the last seat!")
                Student.mutex_semaphore.release()

                super().msg("waiting for the exam to start...")
                Person.class_room.seats_semaphore.release()
                Person.class_room.start_exam.acquire()
                super().msg("is taking the exam...")
                self.grade_exam()
                #time.sleep(20)
                #threading.current_thread().wait(timeout=20)
                Person.WAIT_FLAG.wait(timeout=20)

                super().msg("The teacher collected my exam! Leaving the room now...")
                Person.class_room.end_exam.release()

                super().take_break()

            else:
                Person.class_room.missed_students += 1
                Student.mutex_semaphore.release()
                super().msg("I missed the exam :( waiting for the next one...")
                Person.class_room.missed_exam.acquire()

        Person.class_room.i_am_done.release()
        Person.class_room.wait_for_finish.acquire()
        print(super().msg(self.print_grades()))

        Person.class_room.i_am_done.release()
        Person.class_room.wait_for_finish.acquire()

        Student.mutex_semaphore.acquire()
        Student.num_students += 1

        if Student.num_students % Person.class_room.group == 0:
            for _ in range(Person.class_room.group - 1):
                Student.group_semaphore.release()
            Student.remaining_students -= Student.num_students
            super().msg("I am in group " + str(Student.group_number))
            Student.group_number += 1
            Student.mutex_semaphore.release()
        elif Student.remaining_students < Person.class_room.group:
            super().msg("I am in the last group")
            Student.mutex_semaphore.release()
        else:
            Student.temp_group_num = Student.group_number
            Student.mutex_semaphore.release()
            Student.group_semaphore.acquire()
            super().msg("I am in group " + str(Student.temp_group_num))

        Student.mutex_semaphore.acquire()
        Student.leaving_student += 1
        if Student.leaving_student == Person.class_room.num_students:
            super().msg("I am the last to leave! You can go home now Professor!")
        Person.class_room.go_home_prof.release()
        Student.mutex_semaphore.release()
