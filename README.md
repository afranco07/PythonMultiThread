# PythonMultiThread
This project is an example of multithreading in python. Simulates students rushing into a class room and trying to occupy the seats inside the class room. There is a student thread and instructor thread. They share the classroom object in which controls their synchronization. Similar to my java semaphore project.

## Video Walkthrough

![gif file](https://raw.githubusercontent.com/afranco07/PythonMultiThread/master/python_multi_gif.gif)

## Changing the parameters
You can change the number of students and how many students per group in the person.py class:

![person class file](https://raw.githubusercontent.com/afranco07/PythonMultiThread/master/change_parameters_class.png)

The first parameter is the maximum number of seats inside the class room. The second parameter is the total number of student threads in the program. The third parameter how many students per group.

Make sure to also update the NUMBER_OF_STUDENTS if you change the number in the person.py class. It will not work if you don't update in both places.

![main file]()
