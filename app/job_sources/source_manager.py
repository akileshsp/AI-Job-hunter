from concurrent.futures import ThreadPoolExecutor, as_completed

from app.job_sources.greenhouse_api import GreenhouseAPI
from app.job_sources.lever_api import LeverAPI
from app.job_sources.workable_api import WorkableAPI
from app.job_sources.smartrecruiters_api import SmartRecruitersAPI


class SourceManager:

    def __init__(self):

        self.sources = [
            GreenhouseAPI(),
            LeverAPI(),
            WorkableAPI(),
            SmartRecruitersAPI()
        ]

    def _search_source(self, source, keyword, location):

        print(f"🔍 Searching from {source.__class__.__name__}")

        try:
            return source.search(keyword, location)

        except Exception as e:

            print(f"❌ {source.__class__.__name__}: {e}")
            return []

    def search_all(self, keyword, location):

        jobs = []

        with ThreadPoolExecutor(max_workers=len(self.sources)) as executor:

            futures = [
                executor.submit(
                    self._search_source,
                    source,
                    keyword,
                    location
                )
                for source in self.sources
            ]

            for future in as_completed(futures):
                jobs.extend(future.result())

        return jobs