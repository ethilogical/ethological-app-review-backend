import random
import string
import datetime

# Author: Reece Adkins
# Date: 14 July 2020
# Version 0.0
#
# A decision on an app guideline.
class decision_guideline(interaction):
    def __init__(self, app_id, visitor_id, guideline_id, vote):
        super().__init__(self, app_id, visitor_id)
        self.guideline_id = guideline_id
        self.vote = vote

        self.app_id = app_id
        self.visitor_id = visitor_id

        # Store the date and time the interaction happened
        this.date_time_occurred = datetime.datetime.now()
        # Generate a random string ID with 32 characters.
        self.id = ''.join([random.choice(string.ascii_letters 
            + string.digits) for n in range(32)])
