class SearchAggregator:

    def __init__(self, providers):
        self.providers = providers

    def search(self):

        jobs = []

        for provider in self.providers:
            jobs.extend(provider.search())

        return jobs