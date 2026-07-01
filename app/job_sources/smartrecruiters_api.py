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

    def search(self, keyword="", location=""):

        jobs = []

        keyword = keyword.lower().strip()

        for company in self.COMPANIES:

            print(f"🔵 SmartRecruiters :: {company}")

            try:

                response = requests.get(
                    f"https://api.smartrecruiters.com/v1/companies/{company}/postings",
                    timeout=10
                )

                if response.status_code != 200:
                    continue

                data = response.json()

                for item in data.get("content", []):

                    title = item.get("name", "")
                    city = item.get(
                        "location",
                        {}
                    ).get(
                        "city",
                        location
                    )

                    searchable = (
                        title + " " + city
                    ).lower()

                    if keyword:

                        if keyword not in searchable:

                            continue

                    jobs.append(

                        Job(

                            title=title,

                            company=company,

                            location=city,

                            source="SmartRecruiters",

                            url=item.get("ref", ""),

                            description=item.get(
                                "jobAd",
                                ""
                            )

                        )

                    )

            except Exception as e:

                print(e)

        print(f"✅ SmartRecruiters returned {len(jobs)} jobs")

        return jobs