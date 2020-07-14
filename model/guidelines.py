import random
import string

# Author: Reece Adkins
# Date: 14 July 2020
# Version 0.0
#
# Class modeling guidelines for app approval or rejection.
class guidelines:
    def __init__(self, number, short_text, external_url, description):
        self.number = number
        self.short_text = short_text
        self.external_url = external_url
        self.description = description

        # Generate a random string ID with 32 characters.
        self.id = ''.join([random.choice(string.ascii_letters 
            + string.digits) for n in range(32)])
