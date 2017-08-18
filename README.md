# PythonMultiThread
This project is an example of multithreading in python. Simulates students rushing into a class room and trying to occupy the seats inside the class room. There is a student thread and instructor thread. They share the classroom object in which controls their synchronization. Similar to my java semaphore project.

## Running the Program

1. Run the command `python3 main.py`

2. OPTIONAL: Change the parameters for different effects [link](#Changing-the-parameters)

## Video Demo

![gif file](https://raw.githubusercontent.com/afranco07/PythonMultiThread/master/python_multi_gif.gif)

## Changing the parameters
You can change the number of students and how many students per group in the person.py class:
```python
class Person(object):
    """The base class where the instructor and student extend from"""

    class_room = ClassRoom(8, 14, 3)
    TIME = int(time.time() * 1000)
    WAIT_FLAG = threading.Event()
```

The first parameter is the maximum number of seats inside the class room. The second parameter is the total number of student threads in the program. The third parameter how many students per group.

Make sure to also update the NUMBER_OF_STUDENTS in the main.py if you change the number in the person.py class. It will not work if you don't update in both places.
```python
NUMBER_OF_STUDENTS = 14

for index in range(NUMBER_OF_STUDENTS):
    STUDENT_LIST.append(Student())
    STUDENT_LIST[index].start()
```
