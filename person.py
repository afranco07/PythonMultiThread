"""The class where the student and instructor class extend from"""

import threading
import time
from classroom import ClassRoom

class Person(object):
    """The base class where the instructor and student extend from"""

    class_room = ClassRoom(2, 3, 1)
    TIME = int(time.time() * 1000)

    def take_break(self):
        """
        Tells the current thread to take a break of 4 seconds
        """
        self.msg("is taking a break...")
        time.sleep(4)

    def msg(self, message):
        """
        Used to print messages to the screen, all having
        a similar format
        """
        current_time = int(time.time() * 1000)
        print("[" + str(current_time - Person.TIME) + "]" + threading.current_thread().getName() + ": " + message)
