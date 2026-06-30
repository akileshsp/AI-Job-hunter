from app.search.mock_search import MockSearch


class SearchAggregator:
    def __init__(self):
        self.providers = [
            MockSearch()
        ]

    def search_all(self):
        jobs = []

        for provider in self.providers:
            jobs.extend(provider.search())

        return jobs