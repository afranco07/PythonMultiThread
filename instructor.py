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
