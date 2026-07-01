from concurrent.futures import ThreadPoolExecutor, as_completed

from app.job_sources.provider_registry import get_providers


class JobAggregator:

    def __init__(self):

        self.providers = get_providers()

    def _search_provider(self, provider, keyword, location):

        print(f"🚀 {provider.__class__.__name__}")

        try:

            jobs = provider.search(
                keyword,
                location
            )

            print(
                f"✅ {provider.__class__.__name__}: {len(jobs)} jobs"
            )

            return jobs

        except Exception as e:

            print(
                f"❌ {provider.__class__.__name__}: {e}"
            )

            return []

    def search(self, keyword="", location=""):

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

        print(
            f"\n🎯 Total Aggregated Jobs : {len(jobs)}"
        )

        return jobs
    