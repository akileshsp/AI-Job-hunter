from concurrent.futures import ThreadPoolExecutor, as_completed

from app.ats.greenhouse import GreenhouseATS
from app.ats.lever import LeverATS
from app.ats.workable import WorkableATS
from app.ats.smartrecruiters import SmartRecruitersATS


class SearchManager:

    def __init__(self):

        self.providers = [

            GreenhouseATS(),
            LeverATS(),
            WorkableATS(),
            SmartRecruitersATS()

        ]

    def _search_provider(self, provider, keyword, location):

        print(f"🔍 {provider.name}")

        try:

            return provider.search(
                keyword,
                location
            )

        except Exception as e:

            print(f"❌ {provider.name}: {e}")

            return []

    def search(self, keyword, location):

        jobs = []

        with ThreadPoolExecutor(
            max_workers=len(self.providers)
        ) as executor:

            futures = [

                executor.submit(
                    self._search_provider,
                    provider,
                    keyword,
                    location
                )

                for provider in self.providers

            ]

            for future in as_completed(futures):

                jobs.extend(
                    future.result()
                )

        return jobs