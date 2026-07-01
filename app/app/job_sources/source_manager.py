from app.job_sources.greenhouse_api import GreenhouseAPI
from app.job_sources.lever_api import LeverAPI


class SourceManager:

    def __init__(self):

        self.sources = [
            GreenhouseAPI(),
            LeverAPI()
        ]

    def search_all(self, keyword, location):

        jobs = []

        for source in self.sources:

            print(f"🔍 Searching from {source.__class__.__name__}")

            try:
                jobs.extend(
                    source.search(
                        keyword,
                        location
                    )
                )

            except Exception as e:
                print(f"❌ {source.__class__.__name__}: {e}")

        return jobs