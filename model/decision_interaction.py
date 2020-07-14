import random
import string
import datetime

# Author: Reece Adkins
# Date: 14 July 2020
# Version 0.0
#
# A decision on approval or rejection of an app.
class decision_interaction(interaction):
    def __init__(self, app_id, visitor_id, status, justification):
        self.status = status
        self.justification = justification
        self.app_id = app_id
        self.visitor_id = visitor_id

        # Store the date and time the interaction happened
        this.date_time_occurred = datetime.datetime.now()
        # Generate a random string ID with 32 characters.
        self.id = ''.join([random.choice(string.ascii_letters 
            + string.digits) for n in range(32)])
