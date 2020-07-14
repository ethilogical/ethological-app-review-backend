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