from app.providers.base_provider import BaseProvider
from app.core.job_search_engine import JobSearchEngine


class RealJobProvider(BaseProvider):

    def __init__(self):

        self.engine = JobSearchEngine()

        # Temporary (we'll replace this with AI profile queries later)
        self.keywords = [
            "Packaging Designer"
        ]

        self.locations = [
            "Bengaluru"
        ]

    def search(self):

        jobs = []

        for location in self.locations:

            print(f"\n📍 {location}")

            for keyword in self.keywords:

                print(f"🔎 {keyword}")

                jobs.extend(
                    self.engine.search(
                        keyword,
                        location
                    )
                )

        return jobs