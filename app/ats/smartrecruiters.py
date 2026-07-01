from app.ats.base_ats import BaseATS
from app.job_sources.smartrecruiters_api import SmartRecruitersAPI


class SmartRecruitersATS(BaseATS):

    def __init__(self):

        super().__init__()

        self.api = SmartRecruitersAPI()

    def search(self, keyword, location):

        return self.api.search(
            keyword,
            location
        )