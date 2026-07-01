import requests

from app.job_sources.base_job_source import BaseJobSource
from app.models.job import Job


class SmartRecruitersAPI(BaseJobSource):

    COMPANIES = [
        "Philips",
        "Bosch",
        "Roche",
        "Danaher",
        "Eurofins"
    ]

    def search(self, keyword, location):

        jobs = []

        for company in self.COMPANIES:

            print(f"🔵 SmartRecruiters :: {company}")

            try:

                response = requests.get(
                    f"https://api.smartrecruiters.com/v1/companies/{company}/postings",
                    timeout=20
                )

                if response.status_code != 200:
                    continue

                data = response.json()

                for item in data.get("content", []):

                    city = item.get(
                        "location",
                        {}
                    ).get(
                        "city",
                        location
                    )

                    jobs.append(
                        Job(
                            title=item.get("name", ""),
                            company=company,
                            location=city,
                            source="SmartRecruiters",
                            url=item.get("ref", ""),
                            description=""
                        )
                    )

            except Exception as e:

                print(e)

        print(f"✅ SmartRecruiters returned {len(jobs)} jobs")

        return jobs