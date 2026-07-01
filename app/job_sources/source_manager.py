from concurrent.futures import ThreadPoolExecutor, as_completed
from time import perf_counter

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

        start = perf_counter()

        print(f"\n🚀 {source.__class__.__name__} started")

        try:

            jobs = source.search(
                keyword,
                location
            )

            elapsed = perf_counter() - start

            print(
                f"✅ {source.__class__.__name__} : "
                f"{len(jobs)} jobs "
                f"({elapsed:.2f}s)"
            )

            return jobs

        except Exception as e:

            elapsed = perf_counter() - start

            print(
                f"❌ {source.__class__.__name__} failed "
                f"({elapsed:.2f}s)"
            )

            print(e)

            return []

    def search_all(self, keyword="", location=""):

        jobs = []

        start = perf_counter()

        with ThreadPoolExecutor(
            max_workers=len(self.sources)
        ) as executor:

            futures = {

                executor.submit(
                    self._search_source,
                    source,
                    keyword,
                    location
                ): source

                for source in self.sources

            }

            for future in as_completed(futures):

                try:

                    jobs.extend(
                        future.result()
                    )

                except Exception as e:

                    print(e)

        elapsed = perf_counter() - start

        print(
            f"\n🎯 Total jobs fetched : {len(jobs)}"
        )

        print(
            f"⏱ Total search time : {elapsed:.2f}s\n"
        )

        return jobs