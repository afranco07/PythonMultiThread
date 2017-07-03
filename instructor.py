"""The instructor thread"""

import threading
import time
import random
from person import Person

class Instructor(Person, threading.Thread):

    def __init__(self):
        super(Instructor,self).__init__()
        self.name = "Instructor"

    def run(self):
        random_time = random.randrange(5)
        print("The instructor will arrive in " + str(random_time) + " seconds...")
        time.sleep(random_time)
        print("The instructor is here!")
