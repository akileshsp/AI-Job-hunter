from concurrent.futures import ThreadPoolExecutor, as_completed
from time import perf_counter

from app.job_providers.base_provider import BaseProvider


class ProviderManager:

    def __init__(self, providers: list[BaseProvider]):

        self.providers = providers

    def _run_provider(
        self,
        provider: BaseProvider,
        keyword: str,
        location: str
    ):

        start = perf_counter()

        try:

            jobs = provider.search(
                keyword,
                location
            )

            elapsed = perf_counter() - start

            print(
                f"✅ {provider.name:<20}"
                f"{len(jobs):>5} jobs"
                f"  ({elapsed:.2f}s)"
            )

            return jobs

        except Exception as e:

            elapsed = perf_counter() - start

            print(
                f"❌ {provider.name:<20}"
                f"FAILED ({elapsed:.2f}s)"
            )

            print(e)

            return []

    def search(
        self,
        keyword="",
        location=""
    ):

        jobs = []

        start = perf_counter()

        with ThreadPoolExecutor(
            max_workers=max(1, len(self.providers))
        ) as executor:

            futures = [

                executor.submit(
                    self._run_provider,
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

        elapsed = perf_counter() - start

        print("\n" + "=" * 60)
        print(f"🎯 Total Jobs : {len(jobs)}")
        print(f"⏱ Total Time : {elapsed:.2f}s")
        print("=" * 60)

        return jobs