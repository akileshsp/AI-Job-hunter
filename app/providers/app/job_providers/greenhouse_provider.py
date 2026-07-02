from app.job_providers.base_provider import BaseProvider
from app.job_sources.greenhouse_api import GreenhouseAPI


class GreenhouseProvider(BaseProvider):

    name = "Greenhouse"

    def __init__(self):

        self.api = GreenhouseAPI()

    def search(
        self,
        keyword="",
        location=""
    ):

        return self.api.search(
            keyword,
            location
        )