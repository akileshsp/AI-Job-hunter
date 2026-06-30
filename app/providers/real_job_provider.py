from app.providers.base_provider import BaseProvider
from app.models.job import Job
from app.job_sources.job_api import JobAPI


class RealJobProvider(BaseProvider):

    def __init__(self):
        self.api = JobAPI()

    def search(self):

        jobs = []

        keywords = [
            "Packaging Specialist",
            "Packaging Artwork",
            "Labeling Specialist"
        ]

        for keyword in keywords:

            results = self.api.search(
                keyword,
                "Bengaluru"
            )

            jobs.extend(results)

        return jobs