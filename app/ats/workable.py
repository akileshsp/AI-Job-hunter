from app.ats.base_ats import BaseATS
from app.job_sources.workable_api import WorkableAPI


class WorkableATS(BaseATS):

    def __init__(self):

        super().__init__()

        self.api = WorkableAPI()

    def search(self, keyword, location):

        return self.api.search(
            keyword,
            location
        )