import random
import string

# Author: Reece Adkins
# Date: 14 July 2020
# Version 0.0
#
# Class modeling an app to be approved or denied.
class app:
    def __init__(self, title, img_url, slogan, description):
        self.title = title
        self.img_url = img_url
        self.slogan = slogan
        self.description = description

        # Generate a random string ID with 32 characters.
        self.id = ''.join([random.choice(string.ascii_letters 
            + string.digits) for n in range(32)])
