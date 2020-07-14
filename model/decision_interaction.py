# Author: Reece Adkins
# Date: 14 July 2020
# Version 0.0
#
# A decision on approval or rejection of an app.
class decision_interaction(interaction):
    def __init__(self, app_id, visitor_id, status, justification):
        super().__init__(self, app_id, visitor_id)
        self.status = status
        self.justification = justification
