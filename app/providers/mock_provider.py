from app.models.job import Job
from app.providers.base_provider import BaseProvider


class MockProvider(BaseProvider):

    def search(self):

        return [

            Job(
                title="Senior Packaging Specialist",
                company="Pfizer",
                location="Bengaluru",
                source="Mock",
                url="https://example.com/job1"
            ),

            Job(
                title="Packaging Artwork Specialist",
                company="Viatris",
                location="Bengaluru",
                source="Mock",
                url="https://example.com/job2"
            )

        ]