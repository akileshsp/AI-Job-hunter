from app.job_sources.greenhouse_api import GreenhouseAPI
from app.job_sources.lever_api import LeverAPI
from app.job_sources.workable_api import WorkableAPI
from app.job_sources.smartrecruiters_api import SmartRecruitersAPI

try:
    from app.job_sources.workday_api import WorkdayAPI
except Exception:
    WorkdayAPI = None


class JobAggregator:

    def __init__(self):

        self.providers = [

            GreenhouseAPI(),

            LeverAPI(),

            WorkableAPI(),

            SmartRecruitersAPI()

        ]

        if WorkdayAPI:
            self.providers.append(
                WorkdayAPI()
            )

    def search(self, keyword="", location=""):

        jobs = []

        for provider in self.providers:

            print(
                f"\n🚀 {provider.__class__.__name__}"
            )

            try:

                provider_jobs = provider.search(
                    keyword,
                    location
                )

                print(
                    f"   {len(provider_jobs)} jobs"
                )

                jobs.extend(provider_jobs)

            except Exception as e:

                print(
                    f"❌ {provider.__class__.__name__}"
                )

                print(e)

        print(
            f"\n✅ Aggregated {len(jobs)} jobs"
        )

        return jobs