"""The main function where everything comes together"""

from student import Student
from instructor import Instructor

instructor = Instructor()
student_1 = Student()
student_2 = Student()
instructor.start()
student_1.start()
student_2.start()