from app.ats.base_ats import BaseATS
from app.job_sources.greenhouse_api import GreenhouseAPI


class GreenhouseATS(BaseATS):

    def __init__(self):

        super().__init__()

        self.api = GreenhouseAPI()

    def search(self, keyword, location):

        return self.api.search(
            keyword,
            location
        )