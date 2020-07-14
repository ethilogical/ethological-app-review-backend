import random
import string
import datetime

# Author: Reece Adkins
# Date: 14 July 2020
# Version 0.0
#
# A visitor to the ethical app review website.
class visitor:
    def __init__(self):
        # Store the date and time the visior was created
        this.date_time_created = datetime.datetime.now()
        # Generate a random string ID with 32 characters.
        self.id = ''.join([random.choice(string.ascii_letters 
            + string.digits) for n in range(32)])
