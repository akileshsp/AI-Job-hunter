import requests

from app.job_sources.base_job_source import BaseJobSource
from app.models.job import Job


class WorkableAPI(BaseJobSource):

    COMPANIES = [
        "cookunity",
        "scribbr",
        "virtuagym"
    ]

    def search(self, keyword="", location=""):

        jobs = []

        for company in self.COMPANIES:

            print(f"🟠 Workable :: {company}")

            try:

                response = requests.get(
                    f"https://{company}.workable.com/spi/v3/jobs",
                    timeout=20
                )

                if response.status_code != 200:
                    continue

                data = response.json()

                for item in data.get("results", []):

                    city = location

                    if item.get("location"):
                        city = item["location"].get(
                            "city",
                            location
                        )

                    jobs.append(

                        Job(
                            title=item.get("title", ""),
                            company=company.title(),
                            location=city,
                            source="Workable",
                            url=item.get("url", ""),
                            description=""
                        )

                    )

            except Exception as e:

                print(e)

        print(f"✅ Workable returned {len(jobs)} jobs")

        return jobs