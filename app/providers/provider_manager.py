from app.providers.mock_provider import MockProvider
from app.providers.real_job_provider import RealJobProvider


class ProviderManager:

    def __init__(self):

        self.providers = [
            MockProvider(),
            RealJobProvider()
        ]

    def search_jobs(self):

        jobs = []

        for provider in self.providers:

            print(f"🔍 Searching from {provider.__class__.__name__}...")

            jobs.extend(provider.search())

        return jobs