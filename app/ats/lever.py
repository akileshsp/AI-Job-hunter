from app.ats.base_ats import BaseATS
from app.job_sources.lever_api import LeverAPI


class LeverATS(BaseATS):

    def __init__(self):

        super().__init__()

        self.api = LeverAPI()

    def search(self, keyword, location):

        return self.api.search(
            keyword,
            location
        )