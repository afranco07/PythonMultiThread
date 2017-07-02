"""The class where the student and instructor class extend from"""

from classroom import ClassRoom

import threading

class Person(object):
    """The base class where the instructor and student extend from"""

    class_room = ClassRoom(2, 3, 1)
