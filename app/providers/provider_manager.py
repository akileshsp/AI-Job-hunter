from app.providers.mock_provider import MockProvider
from app.providers.greenhouse_provider import GreenhouseProvider


class ProviderManager:

    def __init__(self):

        self.providers = [
            MockProvider(),
            GreenhouseProvider()
        ]

    def search_jobs(self):

        jobs = []

        for provider in self.providers:
            jobs.extend(provider.search())

        return jobs