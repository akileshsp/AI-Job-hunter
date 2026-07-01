from app.providers.real_job_provider import RealJobProvider
from app.providers.rss_provider import RSSProvider


class ProviderManager:

    def __init__(self):

        self.providers = [
            RealJobProvider(),
            RSSProvider()
        ]

    def search_jobs(self):

        jobs = []
        seen = set()

        for provider in self.providers:

            print(f"\n🔍 Searching from {provider.__class__.__name__}...")

            try:

                provider_jobs = provider.search()

                for job in provider_jobs:

                    key = (
                        job.company.lower(),
                        job.title.lower()
                    )

                    if key not in seen:
                        seen.add(key)
                        jobs.append(job)

            except Exception as e:

                print(f"❌ {provider.__class__.__name__}: {e}")

        return jobs