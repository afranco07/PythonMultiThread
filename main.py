"""The main function where everything comes together"""

from student import Student
from instructor import Instructor

INSTRUCTOR = Instructor()
INSTRUCTOR.start()

STUDENT_LIST = []

NUMBER_OF_STUDENTS = 14

for index in range(NUMBER_OF_STUDENTS):
    STUDENT_LIST.append(Student())
    STUDENT_LIST[index].start()
